from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "giveaway_id"]
        widgets = {
            "content": forms.Textarea(),
            "giveaway_id": forms.HiddenInput()
        }