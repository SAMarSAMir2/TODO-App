from django import forms
from home.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskTitle', 'taskDesc']
        widgets = {
            'taskTitle': forms.TextInput(attrs={'class': 'form-control'}),
            'taskDesc': forms.Textarea(attrs={'class': 'form-control'}),
        }



# from django import forms
# from home.models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['taskTitle', 'taskDesc']