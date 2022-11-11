from django import forms

def ImagegenForm(forms.Form):
    opt = ((('curiosity', 'curiosity')), ('opportunity', 'opportunity'), ('spirit', 'spirit'), ('perserverance', 'perseverance'))
    rover = forms.ChoiceField(label='rover', widget=forms.Select, choices=opt)
    
