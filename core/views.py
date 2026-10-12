from django.shortcuts import render

def home(request):
  context = {
    'page_title': "Codex",
    'cards': None,
  }

  return render(request, 'core/home.html', context)