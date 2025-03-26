def korishlar_soni(request):
    if "read_articles" not in request.session:
        request.session["read_articles"] = []  # Sessiyada bo‘lmasa, bo‘sh ro‘yxat yaratish
    return request.session["read_articles"]
