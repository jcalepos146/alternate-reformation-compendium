from common import E


def D(id, name, st, when, y, sum, body, parties, effect, faith=None, open_q=None, kind="Council or treaty"):
    E(id, "doc", name, st, when, y, sum, body,
      facts=[["Date", when], ["Kind", kind], ["Parties", parties], ["Effect", effect]],
      faith=faith or [], open_q=open_q)


D("lateran-v", "Fifth Lateran Council", "hist", "1512–17", 1512,
  "Reform council that sits before any evangelical movement exists.",
  ["Called by Julius II and closed under Leo X, Lateran V passes reforming decrees that history largely left unenforced. It is the baseline against which the timeline’s changes are measured."],
  "Papacy and bishops", "Reform decrees; curial resistance", faith=["roman-catholic"])

D("concordat-of-bologna", "Concordat of Bologna", "canon", "1516", 1516,
  "Agreement between Leo X and Francis I giving the king nomination of bishops.",
  ["Rome still confirms French bishops under this concordat, which is why it can accept the Lyon primacy. It is the legal basis of the Gallican settlement and the reason the Papacy loses little by it."],
  "Leo X and Francis I", "Crown nominates bishops; pope confirms", faith=["gallican-church", "roman-catholic"])

D("council-of-trent", "Council of Trent", "canon", "1545–63", 1545,
  "The council whose Session 6 allows imputed righteousness in 1547.",
  ["In this timeline Session 6 is softened, allowing imputed righteousness beside inherent righteousness, and Session 5 on original sin stands as written. France never receives the decrees. Historically France delayed reception until the clergy’s declaration of 1615. Here the Gallican settlement exempts it, so communion holds while French doctrine takes its own path.",
   "A proposed driver is the Spirituali party under Pole and Morone, with Contarini’s Regensburg formula as the model."],
  "Pope, legates, bishops", "More Augustinian Roman communion", faith=["roman-catholic"],
  open_q=["Who presides and how the council ends after 1549."])

D("augsburg-interim", "The Augsburg Interim", "canon", "1548–52", 1548,
  "Charles V’s religious settlement after Mühlberg, which splits the Wittenberg movement.",
  ["Enforced by imperial troops in Württemberg and the Upper German cities. Accepted as the Leipzig compromise in Albertine Saxony and Brandenburg, refused in Ernestine Thuringia, Magdeburg, Hamburg, Lübeck, Lüneburg, Mecklenburg and the Neumark."],
  "Emperor and princes", "Splits Philippists and Gnesio-Lutherans", faith=["cranmerian", "gnesio-catholic"])

D("peace-of-augsburg", "Peace of Augsburg", "canon", "1555", 1555,
  "A religious peace that never says which Augsburg Confession it protects.",
  ["The ambiguity sends the question to the Imperial chamber court and to the Diets. Maximilian II’s tolerance keeps that workable until 1576. Rudolf II’s withdrawal lets it fester. Bohemia is where it breaks."],
  "Emperor and Diet", "Ambiguous recognition of the Augsburg Confession", faith=["cranmerian", "gnesio-catholic"])

D("lambeth-council", "Council of Lambeth", "canon", "1549–52", 1549,
  "Cranmer's pan-Protestant council, called because the Schmalkaldic War left no one able to stand alone.",
  ["After the rout of the League ([[schmalkaldic-war]]) the evangelical churches have two choices: submit separately to the Interim, or find a common confession under a prince beyond the Emperor's reach. Cranmer's England is that place. Melanchthon, Bullinger's envoys, Vermigli, à Lasco and Bucer (who dies in 1551) sit with the English bishops. The council produces the agreed confession of the Cranmerian communion and the eucharistic [[lambeth-formula]].",
   "Calvin, Beza and the Geneva and Scottish churches decline: the formula says too much about the consecration for them ([[hardline-reformed]]). The Gnesio party does not attend, since it holds the bodily presence ([[gnesio-lutherans]]). That leaves the Communion broad but not total."],
  "Cranmer, Melanchthon, Vermigli, à Lasco, Bucer, English bishops", "Agreed confession; the Communion forms; Geneva stays outside",
  faith=["cranmerian", "hardline-reformed"],
  open_q=["Whether the Gnesio party is invited at all.", "How Bullinger's Zurich-descended churches (without Zwingli) are represented."])

D("lambeth-formula", "The Lambeth Formula", "canon", "1552", 1552,
  "The eucharistic compromise: Christ is spiritually present through the Spirit and the consecration, and received to benefit by faith.",
  ["The formula sits between three positions. It rejects transubstantiation and the Lutheran bodily presence (ubiquity). It also rejects pure receptionism, the view that Christ is present only in the faithful receiver's act of receiving. The presence follows the consecration, and does not depend on the worth or faith of the person eating; the benefit does depend on faith.",
   "It is this that the strict Calvinists cannot sign, and why they stay out of the united front ([[hardline-reformed]]). The classical exposition is John Cosin's ([[john-cosin]]), who lived a century later and is proposed as the formula's great interpreter, not its author."],
  "Cranmer and the Lambeth delegates", "Eucharistic settlement of the Communion", faith=["cranmerian"],
  open_q=["Whether Cosin's gloss is bound to the text of 1552."], kind="Confession")

D("capitulation-of-wittenberg", "Capitulation of Wittenberg", "canon", "19 May 1547", 1547,
  "John Frederick surrenders the electorate and Wittenberg to the Emperor.",
  ["The capitulation gives Maurice the electoral title, and the Ernestine line keeps Thuringia. It is the formal end of the League's military resistance ([[schmalkaldic-war]])."],
  "Emperor, John Frederick, Maurice of Saxony", "Electorate to Maurice; Ernestine Thuringia kept", faith=["gnesio-catholic"], kind="Treaty")

D("poissy", "Colloquy of Poissy", "canon", "1561", 1561,
  "The French colloquy that partly succeeds here, giving France a framework for settlement.",
  ["In our history Cardinal Tournon opposed Beza and the colloquy failed. Here it works, and the framework ratified around 1576–77 gives France the Gallican–Augustinian settlement under the Primate of Lyon, with the Cranmerian Huguenots protected. The settlement’s success needs an explanation that the timeline has not yet written."],
  "Crown, Roman and Reformed delegates", "Gallican–Augustinian framework", faith=["gallican-church", "cranmerian"],
  open_q=["What carries Poissy through despite Tournon.", "The exact ratification date."])

D("consensus-of-sandomierz", "Consensus of Sandomierz", "canon", "1570", 1570,
  "Agreement among Polish evangelicals that brings Poland into the Cranmerian communion.",
  ["The Lutherans, Reformed and Brethren agree. In this timeline the Consensus becomes Poland’s entry point into the Cranmerian–Philippist Communion."],
  "Polish evangelical churches", "Poland joins the Communion", faith=["cranmerian"])

D("warsaw-confederation", "Warsaw Confederation", "canon", "1573", 1573,
  "The Polish pledge of religious toleration, here naming Gnesio-Catholic congregations.",
  ["Historically the Confederation was a general pledge of peace between confessions. In this timeline Ducal Prussia’s Gnesio-Catholic church is named under Polish overlordship, and a recognised bishopric in Lithuania gives a bridge toward Russia."],
  "Polish nobility", "Toleration, with Gnesio-Catholic recognition", faith=["gnesio-independent"])

D("bohemian-union-1575", "The Bohemian Union", "canon", "1575", 1575,
  "The union of the Utraquists with the Gnesio-Catholics that fixes the church’s name and theology.",
  ["Bohemia’s Utraquists unite with the Gnesio-Lutherans, and the Unity of the Brethren goes to Cranmer. The union makes Bohemia the largest Gnesio-Catholic stronghold. It is the moment the name ‘Gnesio-Catholic’ comes into use, with seven sacraments and the Roman ordination formula."],
  "Utraquists and Gnesio-Lutherans", "Gnesio-Catholic church formed", faith=["gnesio-catholic", "utraquist-rite", "unity-brethren"])

D("red-book", "The Red Book of Sweden", "canon", "1576", 1576,
  "John III’s liturgy, which leans toward the ancient church.",
  ["The Red Book moves Sweden toward Gnesio-Catholicism. The Uppsala Synod of 1593 completes the work."],
  "King John III", "Liturgy moves Sweden toward Gnesio-Catholicism", faith=["gnesio-independent"])

D("uppsala-synod", "Synod of Uppsala", "canon", "1593", 1593,
  "The synod that settles Sweden’s church.",
  ["Under Archbishop Abraham Angermannus the synod fixes Sweden as Gnesio-Catholic. Duke Charles later defends the settlement against Sigismund."],
  "Church of Sweden", "Gnesio-Catholic Sweden", faith=["gnesio-independent"])

D("brest", "Union of Brest", "canon", "1596", 1596,
  "The union of Ruthenian bishops with Rome.",
  ["Occurs as in history. The bishops accept union. Many parishes, the Lviv brotherhood and the Ostroh circle do not. Moscow’s Western-Rite church is its mirror: a Western liturgy inside Orthodoxy."],
  "Ruthenian bishops and Rome", "Uniate Church formed", faith=["ruthenian-uniate", "eastern-orthodox"])

D("xanten", "Treaty of Xanten and the Neuburg Conversion", "canon", "1613–14", 1613,
  "The partition of Jülich-Cleves, with Neuburg turning Gnesio-Catholic under Lyon.",
  ["Wolfgang Wilhelm of Neuburg converts to the Gnesio-Catholic church in 1613 to win French backing. Neuburg takes Jülich and Berg under Lyon, and Cleves and Mark go to Brandenburg. Henry IV’s assassination in 1610 means France arrives through Lyon rather than at the head of an army."],
  "Neuburg, Brandenburg, France", "Jülich-Berg to Neuburg; Cleves-Mark to Brandenburg", faith=["gnesio-lyon"])

D("stolbovo", "Treaty of Stolbovo", "canon", "1617", 1617,
  "Sweden takes Narva and Ingria, and treaty-protects the Western-Rite primate.",
  ["An Orthodox see survives inside Gnesio-Catholic Sweden as a working bridge. Uppsala and Moscow both have reasons to keep it alive."],
  "Sweden and Russia", "Narva to Sweden; primate protected", faith=["western-rite-orthodox", "gnesio-independent"])

D("filaret-catechism", "Filaret’s Catechism", "canon", "1627", 1627,
  "The Russian church’s catechism, in Gnesio-influenced terminology.",
  ["Adopted under Patriarch Filaret as an anti-Latin weapon after the Polish occupation. It teaches penal substitutionary atonement, the material sufficiency of Scripture, the deuterocanon as apostolic tradition from the Second Temple, and dual imputation. Concupiscence as formally sinful is not allowed.",
   "Greek patriarchs condemn the formulas without breaking communion. Kiev-trained clergy resist."],
  "Moscow Patriarchate", "Russian church takes a Gnesio-influenced theology", faith=["russian-orthodox"], kind="Document",
  open_q=["How the catechism reconciles substitution with union with God."])

D("peace-of-prague", "Peace of Prague", "hist", "1635", 1635,
  "The peace in which Saxony and Brandenburg leave the war.",
  ["Both Cranmerian electors make peace with the Emperor as in history, so the war becomes France and Sweden against the Habsburgs."],
  "Emperor, Saxony, Brandenburg", "Cranmerian electors leave the war", faith=["cranmerian"])

D("peace-1648", "The Peace of 1648", "prop", "1648", 1648,
  "Proposed: the settlement that ends the great war, with Lyon named a guarantor.",
  ["Canon records Lyon as a guarantor of the peace. What the peace recognises is not fixed. The first proposal is Rome, the Cranmerian communion and the churches under Lyon’s protection, which would leave independent Gnesio-Catholics without standing in the Empire and push them to accept Lyon’s protection or to emigrate."],
  "Great powers", "Lyon a guarantor; confessions to be fixed", faith=["roman-catholic", "cranmerian", "gnesio-lyon"],
  open_q=["Which confessions have legal standing in the Empire.", "What normative year applies."])

D("pereiaslav", "Pereiaslav Union", "canon", "1654", 1654,
  "The union of the Cossack host with Moscow.",
  ["Happens as in history. Moscow absorbs Kiev’s critics of the catechism, and Kiev-trained clergy become an opposition inside the Russian church. A compromise revision in about 1685 leaves a small break."],
  "Cossacks and Moscow", "Kiev under Moscow", faith=["russian-orthodox", "eastern-orthodox"])

D("catechism-1685", "Revised Catechism of 1685", "canon", "c.1685", 1685,
  "A compromise revision of the Russian catechism, with a small break.",
  ["The revision answers the resisters inside the church. A small group still breaks away. The terms of the compromise are not yet written."],
  "Moscow Patriarchate", "Compromise revision; small break", faith=["russian-orthodox"], kind="Document",
  open_q=["What exactly is revised and who leaves."])

D("torda", "Edict of Torda", "hist", "1568", 1568,
  "Transylvania’s edict protecting preaching.",
  ["John Sigismund’s Diet at Torda protects the preaching of the Gospel as each community understands it. Transylvania recognises Roman, Cranmerian and Unitarian churches, with Gnesio-Catholics a possible fourth."],
  "Transylvanian Diet", "Toleration", faith=["unitarian"])

D("edict-for-huguenots", "Edict Protecting Cranmerian Huguenots", "canon", "c.1598", 1598,
  "Henry IV’s edict for the Cranmerian Huguenots.",
  ["Date and name are not fixed. Nothing is revoked in this timeline, and in 1685 the Cranmerian Huguenots are still protected."],
  "Henry IV and the Huguenots", "Toleration for Cranmerian Huguenots", faith=["gallican-church", "cranmerian"],
  open_q=["Name and date of the edict."])
