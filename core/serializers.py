# core/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Student, Instructor

User = get_user_model()

class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    age = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2","phone_number","adress","age"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        if attrs["age"] < 10 or attrs["age"] > 18:
            raise serializers.ValidationError({"age": "Student age must be between 10 and 18"})
        return attrs

    def create(self, validated_data):
        age = validated_data.pop("age")
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data, is_student=True)
        Student.objects.create(user=user, age=age)
        return user
    


class InstructorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    age = serializers.IntegerField(required=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    expertise = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "age", "bio", "phone_number","adress","expertise"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        if attrs["age"] < 18:
            raise serializers.ValidationError({"age": "Instructor must be at least 18 years old"})
        return attrs

    def create(self, validated_data):
        age = validated_data.pop("age")
        bio = validated_data.pop("bio", "")
        expertise = validated_data.pop("expertise", "")
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data, is_instructor=True)
        Instructor.objects.create(user=user, age=age, bio=bio, expertise=expertise)
        return user
