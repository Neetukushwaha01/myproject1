from django.shortcuts import render


def home_page(request):
    dic = {}
    if request.method == "POST":
        s1 = eval(request.POST.get("subject1"))
        s2 = eval(request.POST.get("subject2"))
        s3 = eval(request.POST.get("subject3"))
        s4 = eval(request.POST.get("subject4"))
        t = s1 + s2 + s3 + s4
        p = t * 100 / 400;
        if p >= 50:
            d = "first div"
        elif p >= 48:
            d = "second div"
        elif p > 35:
            d = "third div"
        else:
            d = "fail"
            data = {
                'total': t,
                'per': p,
                'div': d
            }

    return render(request, "home.html", dic)
