from common import E

H = "hist"


def B(id, name, st, when, y, sum, body, place, sides, result, faith=None, open_q=None):
    E(id, "battle", name, st, when, y, sum, body,
      facts=[["Date", when], ["Place", place], ["Sides", sides], ["Result", result]],
      faith=faith or [], open_q=open_q)


B("marignano", "Battle of Marignano", "canon", "13–14 September 1515", 1515,
  "The French victory over the Swiss in which Zwingli, serving as chaplain, dies. This is the timeline’s point of divergence.",
  ["Francis I defeats the Swiss pikemen near Milan. Huldrych Zwingli was present as chaplain to the Glarus troops in real history and survived. Here he dies, and with him the Zurich reformation of 1519–25. Switzerland stays Roman in 1525, and Reformed theology runs instead through Bucer, Oecolampadius and Calvin.",
   "It also ends the first Anabaptist circle, which formed around Zwingli’s own students, and removes the Kappel Wars. The Catholic inner cantons and the Reformed cantons simply coexist."],
  "Near Milan", "France and Venice against the Swiss Confederacy", "French victory; Zwingli killed",
  faith=["roman-catholic"])

B("pavia", "Battle of Pavia", H, "24 February 1525", 1525,
  "Imperial victory that captures Francis I.",
  ["Charles V’s forces take the king of France prisoner. The map for 1525 is otherwise historical apart from Switzerland."],
  "Pavia, Lombardy", "Empire and Spain against France", "Imperial victory", faith=["roman-catholic"])

B("schmalkaldic-war", "Schmalkaldic War", "canon", "1546–47", 1546,
  "The campaign in which the Emperor destroys the Schmalkaldic League, and the shock that sends the evangelical churches to Lambeth.",
  ["In our history the League's collapse was real but partial, and Charles V's victory left the evangelical princes divided and resentful. In this timeline it is complete. The Danube campaign of 1546 scatters the South German contingents, and Mühlberg ([[muhlberg]]) destroys the Saxon field army in one morning. John Frederick is captured, Philip of Hesse surrenders, and Wittenberg capitulates on 19 May 1547 ([[capitulation-of-wittenberg]]).",
   "The rout is the argument for union. Luther is dead (February 1546), no evangelical prince can field an army alone, and the Interim ([[augsburg-interim]]) is imposed on the beaten. Cranmer's invitation to a council in England ([[lambeth-council]]) is accepted by churches that a year earlier would not have met. Rome is hit as well: the Emperor's win lets Trent soften its decree on justification rather than harden it, because Charles needs a settlement he can enforce ([[council-of-trent]])."],
  "South Germany and Saxony", "Emperor Charles V and Maurice of Saxony against the Schmalkaldic League",
  "Imperial victory, complete; League dissolved",
  faith=["cranmerian", "gnesio-catholic", "roman-catholic"],
  open_q=["Whether Maurice of Saxony still turns on the Emperor in 1552 ([[peace-of-passau]])."])

B("muhlberg", "Battle of Mühlberg", "canon", "24 April 1547", 1547,
  "The decisive battle of the Schmalkaldic War: the Saxon army is destroyed and John Frederick captured.",
  ["Charles V's Spanish and German troops under Alba ([[alba]]) cross the Elbe at dawn and catch the Saxon army on the retreat. It is a rout, not a pursuit-after-a-draw. John Frederick is wounded and taken, and Wittenberg falls within a month.",
   "The League does not recover. Maurice of Saxony takes the electorate. The Ernestines keep Thuringia, the future Gnesio heartland."],
  "Saxony, on the Elbe", "Empire against the Schmalkaldic League", "Overwhelming imperial victory; John Frederick captured",
  faith=["gnesio-catholic", "cranmerian"])

B("siege-magdeburg", "Siege of Magdeburg", "canon", "September 1550 – November 1551", 1550,
  "The city refuses the Interim and is besieged, while Flacius’s presses print the case against it.",
  ["Magdeburg is the Gnesio refusal made into a siege. Maurice of Saxony, now elector, brings the imperial ban down on it. The city stays a Gnesio enclave."],
  "Magdeburg", "Magdeburg against Maurice of Saxony", "Negotiated end; city keeps its confession",
  faith=["gnesio-catholic"])

B("grumbach-feud", "Grumbach Feud", "canon", "1563–67", 1567,
  "The crisis that breaks the Ernestine line and splits Thuringia.",
  ["Wilhelm von Grumbach’s feud draws Duke John Frederick II of Saxe-Gotha into rebellion, and imperial execution follows. After it Weimar and Jena stay Gnesio-Catholic while Gotha and Coburg become Philippist. The timeline must also avert Elector August’s later purge of Jena."],
  "Thuringia", "Ernestine rebels against the Emperor and Elector August", "Ernestines defeated; Thuringia split",
  faith=["gnesio-independent"],
  open_q=["How the 1573 purge of Jena is averted."])

B("lepanto", "Battle of Lepanto", H, "7 October 1571", 1571,
  "Holy League naval victory over the Ottomans.",
  ["The Holy League defeats the Ottoman fleet in the Gulf of Patras. The map treats the Mediterranean as historical outside the Bohemian and Hungarian frontier."],
  "Gulf of Patras", "Holy League against the Ottoman Empire", "League victory", faith=["roman-catholic"])

B("dutch-revolt", "The Revolt of the Netherlands", "canon", "1568–1648", 1568,
  "The long war that splits the Low Countries three ways.",
  ["North: a Cranmerian republic of the United Provinces. South: Spanish Brabant, Flanders and Luxembourg, with Baianist Louvain and Ghent tolerated. Artois, Hainaut, Tournai and Cambrai are a French protectorate. The Dutch–Spanish war resumes in 1621."],
  "Low Countries", "United Provinces against Spain", "Three-way division by 1600",
  faith=["cranmerian", "roman-catholic"])

B("livonian-war", "Livonian War", "canon", "1558–83", 1558,
  "The war that deports Dorpat’s inhabitants into Russia and fixes the Baltic border.",
  ["The deportees of Dorpat later become the core of the Western-Rite church. At the 1583 peace Russia keeps Narva and Ivangorod but loses Dorpat. Sweden takes Estonia around Reval, which makes Swedish Estonia the Gnesio-Catholic route east."],
  "Livonia", "Russia against Poland-Lithuania and Sweden", "Russia keeps Narva; loses Dorpat",
  faith=["western-rite-orthodox"])

B("long-turkish-war", "Long Turkish War", H, "1593–1606", 1593,
  "Habsburg–Ottoman war in Hungary ending at Zsitvatorok.",
  ["The war ends in the peace of Zsitvatorok (1606), which the frontier in this timeline keeps. It occupies Rudolf II as Bohemia’s confessional dispute festers."],
  "Hungary", "Habsburgs against the Ottomans", "Inconclusive; Zsitvatorok", faith=["roman-catholic", "sunni"])

B("polish-occupation-moscow", "Polish Occupation of Moscow", H, "1610–12", 1610,
  "The occupation that drives the anti-Latin turn in Russian theology.",
  ["The Polish garrison holds the Kremlin until a Russian army expels it in 1612. The humiliation is the motive for Filaret’s catechism, which uses Lutheran categories as an anti-Latin weapon. The Western-Rite church stays loyal to Moscow in 1612."],
  "Moscow", "Poland-Lithuania against Russian forces", "Poles expelled",
  faith=["russian-orthodox", "western-rite-orthodox"])

B("defenestration-1618", "Defenestration of Prague", H, "23 May 1618", 1618,
  "The moment the estates cast Habsburg officials from Hradčany Castle.",
  ["The deposition of Ferdinand follows, and the estates elect Frederick V in 1619. The war that follows is three-sided: Rome, the Cranmerian communion and the Gnesio-Catholics."],
  "Prague", "Bohemian estates against the Habsburg regents", "Revolt begins",
  faith=["gnesio-catholic"])

B("white-mountain", "Battle of White Mountain", "canon", "8 November 1620", 1620,
  "The Habsburg–League victory that returns Bohemia to Rome.",
  ["Frederick V’s army is routed outside Prague. The Habsburgs win, Bohemia is returned to Rome by 1635, and Gnesio-Catholic exiles flood Saxe-Weimar, Poland, Sweden and Russia’s Western-Rite church. The moderates make terms: communion in both kinds and a vernacular Mass in return for full union with Rome. Budovec is executed in 1621."],
  "Near Prague", "Habsburgs and Catholic League against the Bohemian estates", "Habsburg victory",
  faith=["gnesio-catholic", "utraquist-rite"])

B("la-rochelle", "Siege of La Rochelle", H, "1627–28", 1627,
  "The fall of the hardline Huguenots’ main fortress.",
  ["After La Rochelle falls the hardline Reformed shrink to the Cévennes and Béarn’s mountains. Cranmerian Huguenots are protected and nothing is revoked."],
  "La Rochelle", "France against the Huguenots", "Royal victory",
  faith=["hardline-reformed", "gallican-church"])

B("breitenfeld", "Battle of Breitenfeld", H, "17 September 1631", 1631,
  "Swedish victory that opens Germany to Gustavus Adolphus.",
  ["Sweden enters the German war as protector of the Gnesio-Catholics, though France leads the anti-Habsburg side as protector of the Lyon-aligned churches."],
  "Near Leipzig", "Sweden and Saxony against the Empire", "Swedish victory", faith=["gnesio-independent"])

B("lutzen", "Battle of Lützen", H, "16 November 1632", 1632,
  "Swedish victory in which Gustavus Adolphus is killed.",
  ["The king’s death leaves Sweden under a regency of Oxenstierna in the name of Christina."],
  "Near Lützen", "Sweden against the Empire", "Swedish victory; Gustavus Adolphus killed",
  faith=["gnesio-independent"])

B("polyanovka", "Smolensk War and the Peace of Polyanovka", H, "1632–34", 1634,
  "Russia’s failed siege of Smolensk, ending in Polish gains.",
  ["Poland keeps Smolensk. The war leaves Poland strong on the eastern frontier as Russia’s catechism sets it further from the Greek world."],
  "Smolensk", "Russia against Poland-Lithuania", "Russian siege fails; Poland keeps Smolensk",
  faith=["russian-orthodox"])

B("nordlingen", "Battle of Nördlingen", H, "5–6 September 1634", 1634,
  "Imperial victory that breaks the Swedish position in south Germany.",
  ["Württemberg is occupied by imperial troops after it. Saxony and Brandenburg make peace at Prague the next spring, and France leads the war."],
  "Nördlingen", "Empire and Spain against Sweden and German allies", "Imperial victory", faith=["roman-catholic"])

B("english-war", "The English War", "canon", "c.1640–1660", 1640,
  "A two-stage civil war in which the reforming crown and Parliament face the establishment, the nobility and the Navy.",
  ["First the Royalists fight in the king’s name against his ministers. Then, once the king openly sides with the Commons, they back a rival Stuart. A West Country minority, the [[byzantinists]], holds the west and considers talks with the Greeks. Canon records a Royalist restoration by 1660 and a conservative French-aligned monarchy afterward, ending in union with a Dutch dynasty around 1688–89.",
   "The 1648 snapshot shows the war. The 1660 snapshot shows the restoration."],
  "England", "Reforming Crown against Royalists", "Royalist restoration (canon)",
  faith=["cranmerian", "byzantinists"],
  open_q=["The battles themselves: names, sites and commanders are not yet fixed.", "The fate of the king."])

B("pereiaslav-war", "The Khmelnytsky Rising", "canon", "1648–54", 1648,
  "The Cossack rising that ends in the Pereiaslav union with Moscow.",
  ["Khmelnytsky’s rising begins in 1648 as in history. Pereiaslav in 1654 ([[pereiaslav]]) puts Kiev under Moscow, which absorbs the Kievan critics of the catechism."],
  "Ukraine", "Cossacks against Poland-Lithuania", "Union with Muscovy, 1654",
  faith=["eastern-orthodox", "russian-orthodox"])

B("deluge", "The Deluge", "canon", "1655–60", 1655,
  "The Swedish and Russian invasions of Poland-Lithuania.",
  ["Polish toleration survives the Deluge, and Kaunas emerges stronger in this timeline. The war strengthens the Gnesio-Catholic bishopric’s position."],
  "Poland-Lithuania", "Poland against Sweden and Russia", "Poland survives; toleration intact",
  faith=["gnesio-independent"])

B("great-turkish-war", "The Great Turkish War", "prop", "1683–99", 1683,
  "Proposed: the Habsburg reconquest of Hungary, ending at Karlowitz.",
  ["The 1700 snapshot shows the Habsburg reconquest after Karlowitz. This entry is a placeholder that follows the history of the same name."],
  "Hungary and the Balkans", "Holy League against the Ottoman Empire", "Habsburg reconquest of Hungary",
  faith=["roman-catholic", "sunni"])
