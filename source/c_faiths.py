from common import E

# ---------------------------------------------------------------- Roman and Roman-adjacent

E("roman-catholic", "faith", "Roman Communion", "canon", "to 1789", 1500,
  "The communion under papal obedience, made more Augustinian by a softened Council of Trent and loosened at its French edge by the Lyon settlement.",
  [
   "In 1500 the Roman communion holds almost all of Latin Christendom. The timeline’s first fork comes inside it: [[council-of-trent]] adopts a softer Session 6 in 1547, allowing imputed righteousness to stand beside inherent righteousness, while Session 5 on original sin stays as written. The result is a Roman church that can read much of the evangelical case on justification inside its own bounds.",
   "France stays in communion but never receives the Tridentine decrees. Rome still confirms French bishops under the [[concordat-of-bologna]], and the [[gallican-church]] runs its own doctrinal track under the Primate of Lyon. Louvain and Ghent teach a Baianist theology that the hierarchy tolerates ([[baianists]]).",
   "Rome gains two Eastern or Western-rite bodies by union: the [[ruthenian-uniate]] church (Brest, 1596) and, after [[white-mountain]], the [[utraquist-rite]] under the Archbishop of Prague. It loses Bohemia’s hardliners to the Gnesio-Catholics and to exile.",
   "Strongholds in 1635: Spain, Portugal, most of Italy, the Habsburg hereditary lands, Bavaria and the Rhenish prince-bishoprics, Poland-Lithuania’s Latin core, Ireland’s population, and New Spain.",
  ],
  facts=[["Head", "Pope (Urban VIII in 1635)"], ["Authority", "Scripture and tradition, papal primacy"],
         ["Justification", "Trent Session 6 (1547): imputed and inherent righteousness together"],
         ["Sacraments", "Seven"], ["Liturgy", "Latin Mass; Utraquist and Greek rites by union"],
         ["Map colour", "CAT gold"]],
  rel=[["gallican-church", "Same communion; Lyon holds appeals and convenes the French synod."],
       ["utraquist-rite", "United after 1620; chalice and vernacular Mass granted for papal primacy."],
       ["gnesio-catholic", "Not in communion. Rome tolerates both the Utraquist union and Lyon’s Gnesio-Catholic ties, which is a standing contradiction."],
       ["cranmerian", "Not in communion; main opponent in the Empire and the Low Countries."]],
  color="#E3C25B",
  open_q=["The papal succession after Paul III is not written. Which popes follow, and do any of them reopen Trent?"])

E("gallican-church", "faith", "Gallican–Augustinian Church", "canon", "1561–1789", 1561,
  "France’s church in Roman communion, led by the Primate of Lyon, with its own Augustinian theology and no Tridentine decrees.",
  [
   "The Colloquy of Poissy ([[poissy]], 1561) partly succeeds here, and a framework ratified around 1576–77 gives France a Gallican–Augustinian settlement. Rome confirms bishops under the 1516 concordat, so Rome loses little and can accept it. Lyon becomes the court of appeal and the convener of the national synod. [[pierre-d-epinac]] is the first Primate to make the office effective.",
   "The settlement faced real resistance. The Parlement of Paris guards Gallican liberties against any churchman. Rouen and Sens historically refused Lyon’s primacy, and Rouen’s exemption survives as a standing grievance. The king backs Lyon as a counterweight to the Guise family’s power in the church.",
   "Henry IV converts to this church in 1589 and protects the Cranmerian Huguenots by edict. After 1610 Lyon extends its reach across the Rhine: the [[gnesio-lyon]] unions of Jülich and Berg come under it, and in 1648 Lyon is named a guarantor of the peace.",
  ],
  facts=[["Head", "Primate of the Gauls at Lyon (Cardinal Alphonse de Richelieu in 1635)"], ["Communion", "Roman, by the concordat"],
         ["Theology", "Augustinian; Baianist schools tolerated"], ["Trent", "Decrees never received"],
         ["Map colour", "GAL pale gold"]],
  rel=[["roman-catholic", "In communion; Rome confirms French bishops."],
       ["gnesio-lyon", "Protects the Rhineland Gnesio-Catholic unions without absorbing them."],
       ["cranmerian", "Protects Cranmerian Huguenots by royal edict."]],
  color="#F1E1A6",
  open_q=["Rouen’s exemption from the Lyon primacy is unresolved.", "How Gallican doctrine on grace differs from Baianist teaching at Louvain."])

E("utraquist-rite", "faith", "Utraquist Rite in Union with Rome", "canon", "1620–1789", 1620,
  "Bohemian Utraquists who accepted papal primacy after White Mountain in return for the chalice and a vernacular Mass.",
  [
   "Before 1618 the Utraquists had merged with the Gnesio-Catholics (the [[bohemian-union-1575]]). After the defeat of the estates, the moderates make terms with Rome. The price is full union and papal primacy. The prize is communion in both kinds and a vernacular Mass, under the Archbishop of Prague, [[harrach]].",
   "The model is the Union of Brest, but in a Western rite. It is possible because Trent’s softened Session 6 lets Gnesio justification be read inside Roman bounds, and the Gnesio-Catholics already hold seven sacraments and the Roman ordination formula.",
  ],
  facts=[["Head", "Archbishop of Prague"], ["Liturgy", "Vernacular Mass, chalice for laity"], ["Map colour", "BUR orange"]],
  rel=[["roman-catholic", "United 1620s–1635."], ["gnesio-catholic", "Parted from it at White Mountain; the hardliners went into exile."]],
  color="#D9944A")

# ---------------------------------------------------------------- Gnesio-Catholic family

E("gnesio-catholic", "faith", "Gnesio-Catholic Church", "canon", "1575–1789", 1575,
  "The heirs of the Gnesio-Lutherans: seven sacraments, the first seven councils, historic ordination, justification by faith alone.",
  [
   "The Gnesio-Lutherans of [[flacius]], [[amsdorf]] and Ernestine Thuringia refused both Interims ([[augsburg-interim]]) and hardened against the Philippists. Their union with the Bohemian Utraquists in 1575 ([[bohemian-union-1575]]) fixes the name and the theology together. The legal banner is the original 1530 Augsburg Confession.",
   "The church holds seven sacraments, the first seven ecumenical councils and ordination by bishops in the old succession. Swedish bishops, consecrated in the pre-Reformation line, consecrate the first Gnesio-Catholic bishops. On justification it holds faith alone. On authority it is conciliar and episcopal, and it denies papal primacy. Those points make it a bridge between Rome, the Cranmerians and the Orthodox, and also explain why each kind of reunion would stall.",
   "By 1635 it has divided into three branches that are not yet churches in conflict. [[gnesio-independent]] runs from Uppsala through Saxe-Weimar and Magdeburg. [[gnesio-lyon]] holds Jülich and Berg under Lyon. [[gnesio-orthodox]] means the Western-Rite church at Narva. How those three drift apart is one of the timeline’s defining threads.",
   "Territories in 1635: Sweden, Saxe-Weimar, Magdeburg, Mansfeld, Ducal Prussia, a recognised bishopric in Lithuania, Neuburg’s Jülich and Berg, and exiled Bohemian congregations.",
  ],
  facts=[["Sacraments", "Seven"], ["Councils", "First seven ecumenical"], ["Ordination", "Episcopal, in the old succession via Sweden"],
         ["Justification", "Faith alone"], ["Authority", "Conciliar and episcopal; no papal primacy"],
         ["Banner", "Augsburg Confession of 1530"], ["Map colour", "GNC plum"]],
  rel=[["cranmerian", "Rival Reformation family; the Philippist victory in 1550 shrank the Gnesio party to its core."],
       ["roman-catholic", "Negotiates only on primacy; Session 6 makes justification readable."],
       ["western-rite-orthodox", "Orthodox-aligned branch."],
       ["gallican-church", "Lyon-aligned branch."]],
  color="#6E2C4F",
  open_q=["Whether the first generation of Thuringian clergy, ordained before Swedish bishops were available, were validly ordained.",
          "A Gnesio-Catholic Sweden whose king is suspected of Cranmerian sympathies."])

E("gnesio-independent", "faith", "Independent Gnesio-Catholics", "canon", "1575–1789", 1593,
  "The branch led from Uppsala: Sweden, Saxe-Weimar, Magdeburg, Mansfeld, Prussia and Kaunas.",
  [
   "This branch keeps the church’s own synodal order. [[uppsala-synod]] (1593) and the Red Book of 1576 ([[red-book]]) set the Swedish pattern. Saxe-Weimar’s bishop sits at Jena, Samland’s at Königsberg, Lithuania’s at Kaunas. Sweden guarantees Saxe-Weimar’s independence.",
   "It is the branch most likely to be squeezed. The 1648 settlement names Lyon a guarantor, which pulls the Rhine churches toward [[gnesio-lyon]]. Moscow’s protection of Narva pulls others toward [[gnesio-orthodox]]. What remains independent depends on whether Uppsala stays out of both orbits.",
  ],
  facts=[["Seats", "Uppsala, Jena, Königsberg, Kaunas"], ["Map colour", "GNC plum"]],
  rel=[["gnesio-lyon", "Pulled toward it by France’s wartime leadership."], ["gnesio-orthodox", "Pulled toward it by the Narva treaty."]],
  color="#6E2C4F", branch_of="gnesio-catholic",
  open_q=["Where Sweden stands in the three-way drift after the great war."])

E("gnesio-lyon", "faith", "Lyon-Aligned Gnesio-Catholics", "canon", "1613–1789", 1613,
  "Rhineland Gnesio-Catholics, chiefly Jülich and Berg, in union with Lyon by special arrangement.",
  [
   "Wolfgang Wilhelm of Palatinate-Neuburg converts to the Gnesio-Catholic church in 1613 to win French backing for his Jülich claim ([[wolfgang-wilhelm]]). He takes Jülich and Berg, and Brandenburg takes Cleves and Mark ([[xanten]]). The Düsseldorf bishop is under the Lyon primacy but is not merged into the Gallican Church.",
   "The map shows it as its own jurisdiction. It confirms that Gnesio-Catholics may accept Lyon’s protection without accepting Rome’s primacy.",
  ],
  facts=[["Seat", "Düsseldorf"], ["Overseer", "Primate of Lyon, by special arrangement"], ["Map colour", "LYG mauve"]],
  rel=[["gallican-church", "Lyon is protector and appeal court."]],
  color="#B88A9E", branch_of="gnesio-catholic")

E("gnesio-orthodox", "faith", "Orthodox-Aligned Gnesio-Catholics", "canon", "1596–1789", 1600,
  "The Western-Rite church at Narva and the Gnesio parishes that look east rather than to Rome or Lyon.",
  ["This is the Orthodox end of the three-way drift. It is the same community as the [[western-rite-orthodox]] church seen from the Gnesio side: Western liturgy, an Orthodox creed and episcopate, and a theology close to Gnesio justification. It is the bridge between the Gnesio and Orthodox worlds."],
  facts=[["Seat", "Narva"], ["Communion", "Moscow"], ["Map colour", "WRO blue"]],
  rel=[["western-rite-orthodox", "Same community, seen from the Gnesio side."]],
  color="#8E4A6C", branch_of="gnesio-catholic")

# ---------------------------------------------------------------- Cranmerian and Reformed

E("cranmerian", "faith", "Cranmerian–Philippist Communion", "canon", "1549–1789", 1549,
  "The wide evangelical communion of England, Scandinavia, Brandenburg, Saxony, Poland and the Low Countries, bound by the confession of Cranmer’s council.",
  [
   "Cranmer’s international council sits at Lambeth from 1549 to 1552, with Bucer, à Lasco and Vermigli among the exiles. After the Interim split ([[augsburg-interim]]) the Philippists of Albertine Saxony and Brandenburg join it. It becomes the home of the moderate evangelical majority, from Hemmingsen’s Denmark-Norway to the Hungarian Reformed, who enter through Bullinger’s Second Helvetic Confession.",
   "It holds together rival theologies. Württemberg’s Lutheran teaching on Christ’s bodily presence sits beside Reformed-leaning churches. It is the Lutheran right wing of the communion, and the tension between them is one of its recurring disputes. The [[consensus-of-sandomierz]] brings in Poland, and the Unity of the Brethren ([[unity-brethren]]) joins after Bohemia’s revolt.",
   "In England its senior see is Canterbury. Under a king who favours a low-church settlement and economic reform, the establishment and the nobility lean Royalist, and a West Country party ([[byzantinists]]) looks east. These fights shape the English war of the 1640s ([[english-war]]).",
  ],
  facts=[["Council", "Lambeth, 1549–52"], ["Senior see", "Canterbury"], ["Other centres", "Dresden, Heidelberg, Copenhagen, The Hague, Zurich"],
         ["Authority", "Scripture, with the agreed confession"], ["Map colour", "CRA rose"]],
  rel=[["hardline-reformed", "Rejected the Cranmerian settlement; Scotland, Geneva, Vaud, Béarn."],
       ["gnesio-catholic", "Rival Reformation family."], ["byzantinists", "A Greek-leaning party in the English church."],
       ["unity-brethren", "Joined after 1575."]],
  color="#B04F6E",
  open_q=["How Württemberg’s teaching on the Eucharist fits the communion’s agreed confession."])

E("hardline-reformed", "faith", "Hardline Reformed Churches", "canon", "1550–1789", 1550,
  "The Calvinist churches that refused Cranmer’s settlement: Scotland’s Kirk, Geneva, Vaud, Béarn and the Huguenot south.",
  [
   "Calvin and Beza hold Geneva ([[calvin]], [[beza]]), and Knox and Melville carry the pattern to Scotland ([[knox]]). When Cranmer’s council ([[lambeth-council]]) settles on a broader confession, these churches stand outside it. They are the strict end of the Reformed world: presbyterian order, tight discipline, no bishops.",
   "In France the Huguenots split three ways: hardliners in Béarn, Languedoc and La Rochelle, moderates in Normandy, Poitou and Dauphiné who join the Cranmerians, and a group of nobles and townsmen who reconcile with Lyon. The hardliners are broken by [[la-rochelle]] (1628) and shrink to the Cévennes and Béarn’s mountains.",
   "In Scotland the hardline Kirk is driven underground and run in secret, with ministers meeting in conventicles. Many of its members emigrate to the New World, to Ulster on the way and to New England, where they come to hold congregational polity. The established church of the Scottish crown is in the Cranmerian communion ([[james-vi-i]]).",
  ],
  facts=[["Centres", "Geneva, Edinburgh, Montauban, Nîmes"], ["Order", "Presbyterian"], ["Map colour", "HRF violet"]],
  rel=[["cranmerian", "Outside it by choice."], ["gallican-church", "Source of reconciled Huguenots."]],
  color="#4B3B7A")

E("byzantinists", "faith", "Byzantinist Church Party", "canon", "1610s–1789", 1630,
  "An Anglican party with Greek sympathies, rooted in the West Country, that wants an autocratic Christian monarchy and a church close to the Greeks.",
  [
   "The Byzantinists are Anglicans who look to the Greek Fathers and to Constantinople. In the English struggle they form a third group beside the Reforming Crown and the Royalist establishment. Their political ideal is autocratic government on the model of the Roman and Byzantine empires, with a modernised army. A minority wants the West Country held as an armed stronghold and formal talks with Constantinople, or with Moscow and the Narva primate.",
   "After the war the Byzantinists emigrate. They found a colony in the Chesapeake, taking the place of Catholic Maryland, with clergy under the Bishop of London.",
  ],
  facts=[["Strength", "Devon, Cornwall, Bristol, Exeter, Oxford’s Greek circle"], ["Colony", "St Mary’s City, Chesapeake (1634)"],
         ["Map colour", "BYZ"]],
  rel=[["cranmerian", "A party within the English church."], ["eastern-orthodox", "Sympathy and possible talks."]],
  color="#D9822B",
  open_q=["Whether the West Country stronghold becomes a formal Anglo-Orthodox jurisdiction."])

E("evangelical-unaligned", "faith", "Unaligned Evangelicals", "canon", "1525–1789", 1525,
  "Evangelical churches of Courland and Livonia outside the German disputes.",
  ["A small group on the Baltic edge, untouched by the Philippist–Gnesio quarrel. Prussia was caught up in Osiander’s controversy rather than in that split ([[osiander]]) and later becomes Gnesio-Catholic. Courland and Livonia stay unaligned."],
  facts=[["Map colour", "EVG pink"]], color="#D49AAE")

E("unity-brethren", "faith", "Unity of the Brethren", "canon", "to 1789", 1575,
  "The Bohemian Brethren, who join the Cranmerian communion.",
  ["The Unity of the Brethren is a Bohemian church of the Hussite tradition. A Brethren minister, Jan Rokyta, debated Ivan IV in 1570. After the Bohemian union of 1575 the Brethren go to Cranmer, while the Utraquists go with the Gnesio-Catholics. [[comenius]] is their last great bishop."],
  facts=[["Communion", "Cranmerian"], ["Map colour", "UNI"]],
  rel=[["cranmerian", "Joined after 1575."]], color="#C2603E")

E("unitarian", "faith", "Unitarian Church of Transylvania", "canon", "1568–1789", 1568,
  "The Antitrinitarian church of Transylvania, one of the principality’s recognised religions.",
  ["Under [[ferenc-david]] and with the backing of John Sigismund, the Edict of Torda ([[torda]], 1568) protects preaching. Transylvania recognises Roman, Cranmerian and Unitarian churches, with Gnesio-Catholics a possible fourth. Its Polish cousins are the [[polish-brethren]]."],
  facts=[["Seat", "Kolozsvár"], ["Map colour", "UNT teal"]], color="#2E9CA6")

E("polish-brethren", "faith", "Polish Brethren", "canon", "1565–1789", 1565,
  "The antitrinitarian community of Poland-Lithuania.",
  ["The Polish Brethren stand with the Unitarians of Transylvania as the radical edge of Polish toleration. [[faustus-socinus]] gives them their theology."],
  facts=[["Map colour", "POL"]], color="#2E9CA6")

E("anabaptist", "faith", "Anabaptists and Mennonites", "canon", "1525–1789", 1525,
  "Radical communities of peaceable believers, shown as dots rather than territories.",
  ["With Zwingli dead at Marignano, the first Anabaptist circle around his students never forms in Zurich. Radical reformers such as Hubmaier at Waldshut and Müntzer at Mühlhausen still appear, since neither depended on Zwingli. [[menno-simons]] organises the Mennonites in the north, and Hutterite communities appear on the map."],
  facts=[["Map colour", "ANA dots"]], color="#3D3D3D")

# ---------------------------------------------------------------- Orthodox and Eastern

E("eastern-orthodox", "faith", "Eastern Orthodox Churches", "canon", "to 1789", 1500,
  "The Patriarchates of Constantinople, Peć and Ohrid, plus Kiev’s Orthodox, Georgia and the Eastern patriarchs.",
  [
   "The Orthodox of the Ottoman Empire, Venice and Lithuania look to Constantinople ([[cyril-lucaris]] in 1635), with the Serbian Patriarchate of Peć restored in 1557 and the Archbishopric of Ohrid self-governing. Moscow’s church has been self-governing since 1448 and a patriarchate since 1589, but under Filaret’s catechism it parts doctrinally from the Greeks ([[russian-orthodox]]).",
   "Kiev’s Orthodox, inside Poland-Lithuania, become the bastion of resistance to that catechism under [[peter-mohyla]]. The Greek patriarchs condemn the Russian formulas without breaking communion. The model is the real Lucaris affair, where a Calvin-leaning confession of 1629 was condemned by Greek synods up to Jerusalem in 1672.",
  ],
  facts=[["Heads", "Constantinople, Peć, Ohrid, Kiev (Orthodox metropolitan)"], ["Map colour", "ORT blue"]],
  rel=[["russian-orthodox", "Strained communion over the catechism."], ["ruthenian-uniate", "Split Kiev’s church at Brest."]],
  color="#6E9BC9")

E("russian-orthodox", "faith", "Russian Orthodox Church", "canon", "1448–1789", 1627,
  "The Church of Moscow, which in 1627 adopts Filaret’s catechism: Gnesio terminology, penal substitution, dual imputation.",
  [
   "After the Polish occupation of Moscow in 1610–12, Patriarch [[filaret]] answers Roman and Polish pressure with the catechism of 1627 ([[filaret-catechism]]). It teaches the material sufficiency of Scripture, treats the deuterocanon as Second Temple apostolic tradition rather than Scripture proper, and holds penal substitution and dual imputation: sin imputed to Christ, his righteousness to the believer. It is an indigenous synthesis of Byzantine ecclesiology and Augustinian-Lutheran soteriology rather than a borrowed Western scholasticism.",
   "Dual imputation is allowed. Teaching that concupiscence is formally sinful is not. The catechism has to say how substitution fits the Orthodox language of union with God, and the answer produces new factions inside the church.",
   "Kiev-trained clergy resist. After Pereiaslav ([[pereiaslav]], 1654) Moscow absorbs its main critics, and a compromise revision around 1685 brings a small break. The Western-Rite church ([[western-rite-orthodox]]) stays loyal to Moscow.",
  ],
  facts=[["Head", "Patriarch of Moscow (Joasaph I in 1635)"], ["Catechism", "1627; revised c.1685"],
         ["Authority", "Scripture materially sufficient; the deuterocanon as apostolic tradition"],
         ["Soteriology", "Penal substitution; dual imputation; concupiscence not formally sinful"], ["Map colour", "ORC"]],
  rel=[["eastern-orthodox", "Greek patriarchs condemn the formulas without breaking communion."],
       ["western-rite-orthodox", "In communion; its mirror in the west."]],
  color="#3F6FA6",
  open_q=["Which factions the dual-imputation question creates inside Russian Orthodoxy.", "The size and character of the 1685 break."])

E("western-rite-orthodox", "faith", "Western-Rite Orthodox Church", "canon", "1570s–1789", 1589,
  "A church with a Western liturgy and Orthodox bishops and creed, in communion with Moscow, with its primate at Narva.",
  [
   "It begins with Ivan IV’s experiment in the 1570s, after the 1570 debate with the Brethren minister Jan Rokyta. Deported people of Dorpat are settled in Russia and given a charter. It becomes a vicariate under the new Patriarchate in 1589, and Godunov’s Westernising policy turns it into a church with its own primate around 1600.",
   "The price of Orthodox recognition is steep. The filioque and unleavened bread are given up. Converts are received by chrismation. The primate is a monk. Clergy are ordained by Orthodox bishops. It is the mirror image of Brest, a Western rite inside Orthodoxy beside the Eastern rite inside Rome.",
   "It stays loyal in 1612. At Stolbovo (1617) Sweden takes Narva and treaty-protects the primate, so an Orthodox see survives inside Gnesio-Catholic Sweden. It keeps vicariates in Moscow’s German Quarter, Novgorod and Pskov.",
  ],
  facts=[["Seat", "Narva"], ["Communion", "Moscow"], ["Reception", "Chrismation"], ["Map colour", "WRO"]],
  rel=[["gnesio-orthodox", "The same community, seen as a Gnesio branch."], ["russian-orthodox", "In communion."]],
  color="#2F5C8A",
  open_q=["Whether Narva’s Orthodox primate under Lyon-aligned Sweden strains the treaty.", "Name and background of the primate in 1635."])

E("ruthenian-uniate", "faith", "Ruthenian Uniate Church", "canon", "1596–1789", 1596,
  "The Eastern-rite church of Belarus and Ukraine, united with Rome at Brest.",
  ["The bishops accept union in 1596 ([[brest]]) but many parishes, the Lviv brotherhood and the Ostroh circle do not. The Uniate Metropolitan [[josyf-rutsky]] holds Kiev alongside the Orthodox Metropolitan [[peter-mohyla]], so the same city has two churches."],
  facts=[["Head", "Uniate Metropolitan of Kiev"], ["Communion", "Roman"], ["Map colour", "ECA"]],
  rel=[["eastern-orthodox", "Rival church in the same cities."], ["roman-catholic", "In union."]],
  color="#A9B98A")

# ---------------------------------------------------------------- Islam, Judaism, others

E("sunni", "faith", "Sunni Islam", "hist", "to 1789", 1500,
  "The majority tradition of the Ottoman, Moroccan and North African worlds.",
  ["Ottoman rule over the Mamluk lands (1517) and Suleiman’s legal order under Şeyhülislam Ebussuud ([[ebussuud]]) make this the dominant faith of the eastern Mediterranean. In the west, the Saadian sultans of Morocco conquer Songhai in 1591. Muslims remain in Spain only until the expulsion of the Moriscos (1609–14)."],
  facts=[["Map colour", "SUN green"]], color="#5E9E6E")

E("shia", "faith", "Shia Islam", "hist", "to 1789", 1501,
  "Twelver Shia under the Safavids, and Zaydi Shia in northern Yemen.",
  ["Shah Ismail makes Twelver Shia the state faith in 1501. The Safavids retake Baghdad in 1623 and hold it until 1638. Zaydi imams hold the northern highlands of Yemen."],
  facts=[["Map colour", "SHI dark green"]], color="#2F6E4E")

E("ibadi", "faith", "Ibadi Islam", "hist", "to 1789", 1500,
  "The Ibadi community of Oman and a few North African oases.",
  ["Oman’s Ibadi imamate is shown on the map with Hormuz."],
  facts=[["Map colour", "IBA light green"]], color="#A6CC86")

E("judaism", "faith", "Jewish Communities", "hist", "to 1789", 1500,
  "Jewish communities from Prague and Kraków to Safed, Salonica and Rome, shown as dots on the confession map.",
  ["The great centres are Prague, Kraków, Lwów, Venice, Constantinople, Salonica and Safed. In Poland-Lithuania, the Council of Four Lands governs communal life from the 1580s. [[joseph-karo]] codifies law at Safed. Karaite communities appear in the same dots."],
  facts=[["Map colour", "JEW dots"]], color="#7A4FA3")

E("miaphysite", "faith", "Miaphysite Churches", "hist", "to 1789", 1500,
  "The Coptic, Ethiopian, Armenian and Syriac churches.",
  ["The Coptic Patriarchate of Alexandria and the Ethiopian Church share a jurisdiction on the map. The Armenian Catholicos sits at Etchmiadzin and Cilicia’s at Sis. The Syriac Patriarch is at Mardin. Ethiopia’s emperor Susenyos converts to Rome in 1622 and abdicates in 1632 ([[susenyos]])."],
  facts=[["Map colour", "MIA"]], color="#8E6FB0")

E("church-east", "faith", "Church of the East", "hist", "to 1789", 1500,
  "The East Syriac church of northern Iraq, with its patriarch at Rabban Hormizd.",
  ["Shown as a community dot on the map."], facts=[["Map colour", "COE"]], color="#4B6584")

E("maronite", "faith", "Maronite Church", "canon", "to 1789", 1500,
  "The Maronites of Lebanon, in communion with Rome.",
  ["Corrected in the map project: the Maronites are marked in communion with Rome, not as Miaphysite."],
  facts=[["Seat", "Qannubin"], ["Communion", "Roman"]], color="#E3C25B")

E("traditional-religions", "faith", "Traditional Religions", "hist", "to 1789", 1500,
  "The religions of sub-Saharan Africa, the Americas and the Eurasian steppe.",
  ["Mapped as a single category outside the Christian and Islamic jurisdictions, with Christian and Muslim communities shown as dots where they exist."],
  facts=[["Map colour", "TRA tan"]], color="#C9B79C")
