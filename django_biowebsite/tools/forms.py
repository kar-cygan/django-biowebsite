from django import forms

class SeqContentForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Plain sequence',
                'class': 'form-control'}
        ),
        min_length=5,
        required=True
    )

    word_size = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control'}
        ),
        initial=1,
        required=True
    )

    def clean_sequence(self):
        return self.cleaned_data['sequence'].upper()
    
    def clean_word_size(self):
        word_size = self.cleaned_data['word_size']
        if word_size < 1:
            raise forms.ValidationError('The word size must be greater than or equal to 1.')
        return word_size
    
    def clean(self):
        seq = self.cleaned_data['sequence']
        word_size = self.cleaned_data['word_size']
        if seq and word_size:
            if word_size > len(seq):
                raise forms.ValidationError('The word size cannot be greater than the length of the sequence.')


class RevCompForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Plain sequence',
                'class': 'form-control'}
        ),
        min_length=5,
        required=True
    )

    method = forms.ChoiceField(
        choices=[
            ('reverse', 'Reverse'),
            ('complement', 'Complement'),
            ('reverse_complement', 'Reverse Complement'),
        ],
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    def clean_sequence(self):
        return self.cleaned_data['sequence'].upper()


class TranslationForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Plain DNA sequence',
                'class': 'form-control'}
        ),
        min_length=5,
        required=True
    )
  
    def clean_sequence(self):
        sequence = self.cleaned_data['sequence'].upper()
        nucleotides = {'A', 'C', 'G', 'T'}
        for nt in sequence:
            if nt not in nucleotides:
                raise forms.ValidationError('Incorrect DNA sequence, only characters A, C, T, G allowed.')
        return sequence


class RandomDNAField(forms.FloatField):
    step = 0.01
    
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = forms.TextInput(
            attrs={
                'type': 'number', 
                'step': self.step, 
                'class': 'form-control'
                }
            )
        super().__init__(*args, **kwargs)


class RandomDNAForm(forms.Form):
    seq_len = forms.IntegerField(
        label="Sequence length",
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Sequence length between 20 and 10,000 nucleotides.'}
        ),
        required=True
    )

    freq_a = RandomDNAField(
        label='A frequency',
        initial=0.25
    )

    freq_c = RandomDNAField(
        label='C frequency',
        initial=0.25
    )

    freq_g = RandomDNAField(
        label='G frequency',
        initial=0.25
    )

    freq_t = RandomDNAField(
        label='T frequency',
        initial=0.25
    )

    def clean_seq_len(self):
        seq_len = self.cleaned_data['seq_len']
        if seq_len < 20:
            raise forms.ValidationError('The length of the sequence must be greater than 20.')
        if seq_len > 10000:
            raise forms.ValidationError('The length of the sequence must be less than 10,000.')
        return seq_len
    
    def clean(self):
        freq_a = self.cleaned_data.get('freq_a')
        freq_c = self.cleaned_data.get('freq_c')
        freq_g = self.cleaned_data.get('freq_g')
        freq_t = self.cleaned_data.get('freq_t')

        if freq_a + freq_c + freq_g + freq_t != 1:
            raise forms.ValidationError('The nucleotide frequency must add up to 1.')

