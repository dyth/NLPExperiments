convert(objectPhrase([noun]), objectPhrase(noun)).
convert(relatorPhrase([verb]), relatorPhrase(verb)).
convert(objectPhrase([determiner | T]), objectPhrase(determiner, T1)) :- convert(objectPhrase(T), T1).
convert(objectPhrase([article | T]), objectPhrase(article, T1)) :- convert(objectPhrase(T), T1).
convert(objectPhrase([adjective | T]), objectPhrase(adjective, T1)) :- convert(objectPhrase(T), T1).
convert(relatorPhrase([adverb | T]), relatorPhrase(adverb, T1)) :- convert(relatorPhrase(T), T1).
convert(relatorPhrase(S), relatorPhrase(H1, preposition)) :- append(H, [preposition], S), H \== [], convert(relatorPhrase(H), H1).
convert(objectPhrase(S), objectPhrase(A, B, C)) :- append(H, T, S), T \== [], append(I, J, H), I \== [], J \== [], convert(objectPhrase(I), A), convert(relatorPhrase(J), B), convert(objectPhrase(T), C).
convert(objectPhrase(S), objectPhrase(A, conjunction, B)) :- append(H, [conjunction | T], S), convert(objectPhrase(H), A), convert(objectPhrase(T), B).
convert(relatorPhrase(S), relatorPhrase(A, conjunction, B)) :- append(H, [conjunction | T], S), convert(relatorPhrase(H), A), convert(relatorPhrase(T), B).
convert(sentence(S), sentence(S1)) :- convert(objectPhrase(S), S1).
