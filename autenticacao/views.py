from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

# 🔹 Serializador para Registrar Usuários
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# 🔹 Serializador para Login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Credenciais inválidas.")
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

# 🔹 Endpoint para Registro de Usuários (Público)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # ✅ Permite qualquer pessoa criar conta

# 🔹 Endpoint para Login (Público)
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]  # ✅ Permite qualquer pessoa logar

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# 🔹 Customização do Token JWT (Público)
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]  # ✅ Permite qualquer pessoa logar

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return Response({
                "access": response.data["access"],
                "refresh": response.data["refresh"],
                "message": "Login bem-sucedido!"
            }, status=status.HTTP_200_OK)
        return response

# 🔹 Exemplo de View Protegida (Somente usuários autenticados)
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # 🔒 Somente usuários autenticados

    def get(self, request):
        return Response({"message": "Você está autenticado!"}, status=status.HTTP_200_OK)
