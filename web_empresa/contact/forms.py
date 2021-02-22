from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(min_length=3,max_length=100, label = "nombre", required = True, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder':'Ingresar nombre'}
        ))
    
    email =  forms.EmailField(max_length=100, label = "email", required = True, widget=forms.EmailInput(
        attrs={'class':'form-control', 
               'placeholder': 'Ingresar email'}
        ))
    
    contenido = forms.CharField(min_length=20,max_length=400,label= "contenido", required = True, widget=forms.Textarea(
        attrs={'class':'form-control', 
               'rows': 3,
               'placeholder': 'Ingresar mensaje'}
        )) 