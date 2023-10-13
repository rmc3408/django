from django.forms import ModelForm
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ['user_name', 'email']
        # exclude = ['rating']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        help_texts = {
            "user_name": "Username is required",
        }
        error_messages = {
            "user_name": {
                "required": "and a mandatory field !!",
            },
        }
