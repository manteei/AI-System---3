%База знаний по игре "Эволюция"

%Факты о том, какие виды животных бывают по типу питания
kind_of_nutricion(parasite).
kind_of_nutricion(predator).
kind_of_nutricion(herbivore).
kind_of_nutricion(omnivore).

%Факты о том, какие виды животных бывают по месту обитания
habitat_type(waterfowl).
habitat_type(amphibian).
habitat_type(burrow).
habitat_type(aerobionts).

%Факты о том, как животные взаимодействуют между собой
interaction_type(cooperation).
interaction_type(piracy).
interaction_type(symbiosis).
interaction_type(interaction).

%Факты о том, какие дополнительные качества могут быть
additional_qualities(sharp_vision).
additional_qualities(poisonous).
additional_qualities(tail_flick).
additional_qualities(hibernation).
additional_qualities(big).

%Факты об игроках
player_now(maria).
player_now(vlad).
player_now(maxim).
player_now(lara).

%факты о том, какому игроку какие попались дополнительные качества
player_qualities(maria, sharp_vision).
player_qualities(vlad, tail_flick).
player_qualities(vlad, big).
player_qualities(vlad, hibernation).
player_qualities(lara, poisonous).
player_qualities(lara, tail_flick).

%факты о том, какому игроку какое животное попалось по взаимодействию
player_interaction(maria, interaction).
player_interaction(vlad, symbiosis).
player_interaction(maxim, piracy).
player_interaction(lara, cooperation).

%факты о том, какому игроку какое животное попалось по типу питания
player_nutricion(maria, predator).
player_nutricion(vlad, parasite).
player_nutricion(maxim, herbivore).
player_nutricion(lara, omnivore).

%факт о том на сколько баллов животное агрессивное в зависимости от типа питания
agression(parasite, 2).
agression(predator, 3).
agression(herbivore, 1).
agression(omnivore, 3).

%факты о том, какому игроку какое животное попалось по месту обитания
player_habitat(maria, waterfowl).
player_habitat(vlad, amphibian).
player_habitat(maxim, aerobionts).
player_habitat(lara, burrow).

%правило опредления является ли игрок "паразитом"
is_parasit(Name):-
    player_now(Name),
    player_nutricion(Name, parasite).

%правило определения может ли игрок жить под водой
is_underwater(Name):-
    player_now(Name),
    player_habitat(Name, waterfowl)|player_habitat(Name, amphibian).

%правило подсчета дополнительных качеств по имени игрока 
count_qualities(Name, Count) :-
    findall(Quality, player_qualities(Name, Quality), Qualities),
    length(Qualities, Count).

%правило подсчета баллов "агрессии" игрока
count_attack(Name, Agression):-
    player_now(Name), 
    player_nutricion(Name, Nutricion), 
    agression(Nutricion, Agression).

%правило определения "съест" ли один игрок другого.
will_eat(Name1, Name2):-
    player_now(Name1), 
    player_now(Name2), 
    count_attack(Name1, Agression1),
    count_attack(Name2, Agression2),
    count_qualities(Name1, Quality1),
    count_qualities(Name2, Quality2),
     (Agression1 + Quality1 > Agression2 + Quality2-> true ;  false).

    
    
    
   










