# Rezultāti

## Kas ir šie dati un no kurienes tie nāk?

Tā ir AI4I 2020 Predictive Maintenance Dataset datu kopa no Kaggle.

Datu kopā ir 10000 ierakstu par rūpniecisku iekārtu darbību. Tajā ir informācija par gaisa temperatūru, procesa temperatūru, rotācijas ātrumu, griezes momentu un instrumenta nolietojumu.

Modelis prognozē, vai notiks iekārtas atteice (Machine failure).

## Kas ar datiem bija nepareizi un ko tu ar tiem izdarīji?

Dati tika pārbaudīti uz dublikātiem un trūkstošām vērtībām.

Tika izmantota datu tīrīšana ar drop_duplicates() un dropna() funkcijām.

Pārbaudes laikā tika konstatēts, ka datu kopā ir 10000 ierakstu gan pirms, gan pēc tīrīšanas, tādēļ dati bija pilnīgi.

## Ko modelis prognozē un cik labi? Salīdzini ar bāzes līniju!

Modelis prognozē iekārtas atteici.

Bāzes līnijas precizitāte bija 0.970.

Modeļa precizitāte bija 0.985.

Modelis pārspēja bāzes līniju, tāpēc tas darbojas labāk nekā vienkārša biežākās atbildes minēšana.

## Ja šis modelis strādātu reālā sistēmā, ko tu ar tā prognozi darītu?

Ja modelis prognozētu iespējamu iekārtas atteici, sistēma automātiski izveidotu apkopes pieteikumu.

Tehniķis pārbaudītu konkrēto iekārtu pirms pilnīgas atteices.

## Kas notiek, ja modelis kļūdās?

### Nepamatota trauksme

Iekārta tiek pārbaudīta bez nepieciešamības.

Tas rada papildu darba un apkopes izmaksas.

### Nepamanīta problēma

Iekārtas atteice netiek pamanīta laikus.

Tas var izraisīt ražošanas dīkstāvi vai bojājumus.

Nepamanīta problēma ir sliktāka, jo tās izmaksas parasti ir lielākas.

## Ko ar šo modeli nedrīkst darīt?

Modeli nedrīkst izmantot kā vienīgo pamatu iekārtas nomaiņai.

Prognoze nav garantija, ka atteice noteikti notiks.

## Pašvērtējums

Izdevās sagatavot datus un izveidot strādājošu mašīnmācīšanās modeli.

Neizdevās iegūt pilnīgi precīzu prognozi, jo dati satur nenoteiktību.

Nākamreiz izmēģinātu vairākus dažādus modeļus un salīdzinātu to rezultātus.

