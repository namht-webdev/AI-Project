%base
male(prince_george).
male(prince_phillip).
male(james_viscount_severn).
male(mike_tindall).
male(peter_phillips).
male(prince_harry).
male(prince_william).
male(prince_edward).
male(timothy_laurence).
male(prince_andrew).
male(captain_mark_phillips).
male(prince_charles).
female(queen_elizabeth_ii).
female(princess_diana).
female(camila_parker_bowles).
female(princess_anne).
female(sarah_ferguson).
female(sophie_rhys-jones).
female(kate_middleton).
female(atumn_kelly).
female(zara_phillips).
female(princess_beatrice).
female(princess_eugenie).
female(lady_louise_mountbatten_windsor).
female(princess_charlotte).
female(savannah_phillips).
female(isla_phillips).
female(mia_grace_tindall).
parent(queen_elizabeth_ii,prince_charles).
parent(queen_elizabeth_ii,princess_anne).
parent(queen_elizabeth_ii,timothy_laurence).
parent(queen_elizabeth_ii,prince_andrew).
parent(queen_elizabeth_ii,prince_edward).
parent(prince_phillip,price_charles).
parent(prince_phillip,princess_anne).
parent(prince_phillip,prince_andrew).
parent(prince_phillip,prince_edward).
parent(prince_charles,prince_william).
parent(princess_diana,prince_william).
parent(prince_charles,prince_harry).
parent(princess_diana,prince_harry).
parent(captain_mark_phillips,peter_phillips).
parent(captain_mark_phillips,zara_phillips).
parent(princess_anne,peter_phillips).
parent(princess_anne,zara_phillips).
parent(prince_andrew,princess_beatrice).
parent(prince_andrew,princess_eugenie).
parent(sarah_ferguson,princess_beatrice).
parent(sarah_ferguson,princess_eugenie).
parent(prince_edward,james_viscount_severn).
parent(prince_edward,lady_louise_mountbatten-windsor).
parent(sophie_rhys-jones,james_viscount_severn).
parent(sophie_ryhs-jones,lady_louise_mountbatten-windsor).
parent(prince_william,prince_george).
parent(prince_william,prince_charlotte).
parent(kate_middleton,prince_george).
parent(kate_middleton,prince_charlotte).
parent(peter_phillips,savannah_phillips).
parent(peter_phillips,isla_phillips).
parent(autumn_kelly,savannah_phillips).
parent(autumn_kelly,isla_phillips).
parent(zara_phillips,mia_grace_tindall).
parent(mike_tindall,mia_grace_tindall).
married(queen_elizabeth_ii,prince_phillip).
married(prince_phillip,queen_elizabeth_ii).

married(prince_charles,camilla_parker_bowles).
married(camilla_parker_bowles,prince_charles).

married(princess_anne,timothy_laurence).
married(timothy_laurence,princess_anne).

married(sophie_rhys-jones,prince_edward).
married(prince_edward,sophie_rhys-jones).

married(prince_william,kate_middleton).
married(kate_middleton,prince_william).

married(autumn_kelly,peter_phillips).
married(peter_phillips,autumn_kelly).

married(zara_phillips,mike_tindall).
married(mike_tindall,zara_phillips).

divorced(princess_diana,prince_charles).
divorced(prince_charles,princess_diana).

divorced(captain_mark_phillips,princess_anne).
divorced(princess_anne,captain_mark_phillips).

divorced(sarah_ferguson,prince_andrew).
divorced(prince_andrew,sarah_ferguson).

%tu che
husband(Person,Wife):-male(Person),married(Person,Wife).

wife(Person,Husband):-female(Person),married(Person,Husband).

father(Parent,Child):-male(Parent),parent(Parent,Child).

mother(Parent,Child):-female(Parent),parent(Parent,Child).

child(Child,Parent):-parent(Parent,Child).

son(Child,Parent):-male(Child),parent(Parent,Child).

daughter(Child,Parent):-female(Child),parent(Parent,Child).

grandparent(GP,GC):-parent(GP,Parent),parent(Parent,GC).

grandfather(GF,GC):-grandparent(GF,GC),male(GF).

grandmother(GM,GC):-grandparent(GM,GC),female(GM).

grandchild(GC,GP):- parent(GP, Parent), parent(Parent, GC).
grandson(GS,GP):-grandchild(GS,GP),male(GS).

granddaughter(GD,GP):-grandchild(GD,GP),female(GD).

sibling(Person1,Person2):- father(Father,Person1), mother(Mother,Person1),father(Father,Person2),mother(Mother,Person2),not(Person1=Person2).

brother(Person,Sibling):-sibling(Person,Sibling),male(Person).

sister(Person,Sibling):-sibling(Person,Sibling),female(Person).

aunt(Person,NiceNePhew):-parent(Parent,NieceNephew),((sister(Person,Parent));(brother(Uncle,Parent),wife(Person,Uncle))).

uncle(Person,NiceNePhew):-parent(Parent,NieceNephew), ((brother(Person,Parent));(sister(Aunt,Parent),husband(Person,Aunt))).

nephew(Person,AuntUncle):-(aunt(AuntUncle,Person);uncle(AuntUncle,Person)),male(Person).

niece(Person,AuntUncle):-(aunt(AuntUncle,Person);uncle(AuntUncle,Person)),female(Person).

























