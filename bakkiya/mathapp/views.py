from django.shortcuts import render

def calculate_power(request):
    context = {
        'P': "0",
        'I': "0",
        'R': "0"
    }

    if request.method == 'POST':
        print("POST method is used")
        print('request.POST:', request.POST)

        I = request.POST.get('intensity', '0')
        R = request.POST.get('resistance', '0')

        print('Intensity (I) =', I)
        print('Resistance (R) =', R)

        try:
            intensity = float(I)
            resistance = float(R)
            power = intensity ** 2 * resistance
            context['P'] = round(power, 2)
        except ValueError:
            context['P'] = "Invalid input"

        context['I'] = I
        context['R'] = R
        print('Power (P) =', context['P'])

    return render(request, 'mathapp/math.html', context)
