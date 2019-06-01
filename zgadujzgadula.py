import random

liczbaProb = 0
maxLiczbaProb = 8
liczba = random.randint(1,50)

name = input("Hej! Jak masz na imię? ")

print(name + ", Pomyślałem liczbę od 1 do 50. Jesteś w stanie zgadnąć jaka to liczba?")

while liczbaProb < maxLiczbaProb:
  odpowiedz = input("Zgadnij jaka to liczba... ")
  odpowiedz = int(odpowiedz)

  liczbaProb = liczbaProb + 1;
  guessesLeft = maxLiczbaProb - liczbaProb;

  if odpowiedz < liczba:
    guessesLeft = str(guessesLeft)
    print("Oj, ciut za mała liczba! Próbuj dalej. Masz jeszcze " + guessesLeft + " prób.")

  if odpowiedz > liczba:
    guessesLeft = str(guessesLeft)
    print("Uhuhu, trochę za dużo! Próbuj dalej. Masz jeszcze " + guessesLeft + " prób.")

  if odpowiedz == liczba:
    break

if odpowiedz == liczba:
  liczbaProb = str(liczbaProb)
  print("Woooohooo, dobra robota! Udało Ci się odgadnąć liczbę po " + liczbaProb + " próbach :)")

if odpowiedz != liczba:
  liczba = str(liczba)
  print("Niestety, nie udało się :( Liczba, o której pomyślałem to " + liczba + " :)")