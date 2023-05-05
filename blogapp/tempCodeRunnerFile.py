

def lendCoins(request):

    if request.method == "POST":
        email = request.POST.get('userNameSrch')
        amnt = int(request.POST.get('coins'))
        try:
            user = UserAccount.objects.get(email=email)
            sender = request.user
            if not request.user.is_superuser:
                if sender.coins_scored < amnt:
                    messages.error(request,"Chacha O Chacha your'e short on coins")
                    return render(request,'main/adminTem/lendCoins.html')
                else:
                    sender.coins_scored -= amnt
            user.coins_scored += amnt
            user.save()
            messages.success(request,f"{user.name} coins increased by {amnt}")
            return render(request,'main/adminTem/lendCoins.html')
        except Exception as e:
            messages.error(request,e)
            print(e)
            return render(request,'main/adminTem/lendCoins.html')
    else:
        return render(request,'main/adminTem/lendCoins.html')