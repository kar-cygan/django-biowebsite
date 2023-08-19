from django.shortcuts import render
from .forms import SeqContentForm, RevCompForm, RandomDNAForm, TranslationForm
from . import utils

def seqcontent_view(request):
    if request.method == 'POST':
        form = SeqContentForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            word_size = form.cleaned_data['word_size']

            results = utils.count_words(seq, word_size)
            context = {
                'results': results,
                'seq_len': len(seq),
            }
            return render(request, 'tools/seqcontent.html', context)
    else:
        form = SeqContentForm()
    return render(request, 'tools/seqcontent.html', {'form': form})

def revcomp_view(request):
    if request.method == 'POST':
        form = RevCompForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            method = form.cleaned_data['method']

            if method == 'reverse':
                new_seq = utils.reverse(seq)
            elif method == 'complement':
                new_seq = utils.complement(seq)
            else:
                new_seq = utils.reverse_complement(seq)
            
            context = {
                'seq': seq,
                'method': method,
                'results': new_seq,
            }
            return render(request, 'tools/revcomp.html', context)
    else:
        form = RevCompForm()
    return render(request, 'tools/revcomp.html', {'form': form})

def randomdna_view(request):
    if request.method == 'POST':
        form = RandomDNAForm(request.POST)
        if form.is_valid():
            seq_len = form.cleaned_data['seq_len']
            freq_a = form.cleaned_data['freq_a']
            freq_c = form.cleaned_data['freq_c']
            freq_g = form.cleaned_data['freq_g']
            freq_t = form.cleaned_data['freq_t']

            seq = utils.random_dna(seq_len, freq_a, freq_c, freq_g, freq_t)
            return render(request, 'tools/randomdna.html', {'results': seq, 'seq_len': seq_len})
    else:
        form = RandomDNAForm()    
    return render(request, 'tools/randomdna.html', {'form': form})

def translation_view(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            new_seq = utils.translate(seq)            
            context = {
                'seq': seq,
                'results': new_seq,
            }
            return render(request, 'tools/translation.html', context)
    else:
        form = TranslationForm()
    return render(request, 'tools/translation.html', {'form': form})