"""Decisions taken with the author, applied over the earlier entries.
Each call replaces fields on one entity. Order matters only for the same id."""
from common import ENT, P

_by = {e["id"]: e for e in ENT}


def D(id, st=None, **kw):
    e = _by[id]
    if st: e["st"] = st
    for k, v in kw.items():
        if k == "body" and not isinstance(v, list): v = [v]
        if k == "add_faith": e["faith"] = e["faith"] + [x for x in v if x not in e["faith"]]; continue
        e[k] = v


def fact(id, label, value):
    e = _by[id]
    for r in e["facts"]:
        if r[0] == label: r[1] = value; return
    e["facts"].append([label, value])


# ------------------------------------------------------------------ Scotland
D("knox", open_q=[])

# ------------------------------------------------------------------ Mary I, Cranmer and Pole
D("mary-i-england", "canon", sum="Queen of England 1553–58, who restores Rome as in history.",
  body=["Edward VI dies in 1553 and Mary succeeds. She restores papal obedience, as in history, and the Communion formed at Lambeth ([[lambeth-council]]) is tested at home: the evangelical exiles go to Frankfurt, Strasbourg and Zurich ([[bullinger]]), and Cranmer is burned ([[cranmer]]).",
        "The reign lasts five years. Cardinal Pole ([[reginald-pole]]) is her Archbishop of Canterbury. Elizabeth restores the Communion in 1558 ([[elizabeth-i]]), and the exiles bring back the Zurich and Frankfurt habits that later feed the archpresbyter order ([[cranmerian]])."],
  open_q=[])
D("cranmer", body=["Cranmer's council sits at Lambeth from 1549, with the continental exiles in England ([[lambeth-council]]). His Communion is named for him. He is burned at Oxford in March 1556 under Mary ([[mary-i-england]]), having recanted and then withdrawn the recantation, as in history. His martyrdom is the Communion's founding story in England."],
  open_q=[])
D("reginald-pole", st="prop", body=["Pole was one of the legates at Trent's opening and belonged to the Spirituali ([[spirituali]]). In this timeline he is proposed as a driving voice for imputed righteousness in 1547, a role history did not give him. Under Mary he is Archbishop of Canterbury from Cranmer's death in 1556 until his own in 1558, as in history ([[mary-i-england]])."])

# ------------------------------------------------------------------ The English War
D("english-war", sum="A civil war in two stages: the Royalists, then the Reforming Crown's army, with a king deposed and a Stuart restoration.",
  body=["The Royalists (the bishops, the nobility and the Navy) fight in the king's name against his reforming ministers. When Charles I openly sides with the Commons, they back his son, the future Charles II ([[charles-ii]]). The king is deposed and lives in exile.",
        "A West Country minority, the [[byzantinists]], holds the west. The proposed course: Edgehill is indecisive; the Royalists win at Lansdown and Naseby ([[naseby]]), where the king is deposed; the Reforming Crown's army under Fairfax and Cromwell wins in the north at Marston Moor and Preston ([[preston-1648]]) and holds the country until 1660, when the restoration brings Charles II back and establishes the conservative, French-aligned monarchy. William of Orange ends it by force in 1688 ([[william-iii]]).",
        "The 1648 snapshot shows the war. The 1660 snapshot shows the restoration."],
  result="Charles I deposed and exiled; Royalist restoration under Charles II in 1660",
  open_q=["Whether the proposed course of the battles is acceptable, in particular who holds London between about 1646 and 1660."])
D("charles-i-england", body=["In our history Charles I defended bishops and the royal prerogative. Here the roles are reversed: the king leads the reforming cause and the opposition raises the old constitution. The establishment, the nobility and the Navy lean toward Royalism. A West Country group goes further and argues for an autocratic monarchy on Roman and Byzantine lines ([[byzantinists]]).",
  "By 1635 he is making low-church reform a programme, and war follows around 1640–42 ([[english-war]]). He is deposed after Naseby and lives in exile, in the Dutch Republic or the Palatinate."],
  open_q=["Where he lives in exile, and when he dies."])
D("charles-ii", "canon", sum="Son of the deposed Charles I, backed by the Royalists as rival Stuart and restored in 1660.",
  body=["The Royalists proclaim Charles, the deposed king's son, as the rival Stuart once his father sides with the Commons ([[english-war]]). He is restored in 1660 under a conservative, French-aligned monarchy, with the Royalist establishment and the Byzantinist party in his train ([[byzantinists]]). He reigns until 1685."],
  open_q=[])
D("james-ii", "prop", sum="Charles II's brother, whose reign ends when the Dutch land in 1688.",
  body=["James succeeds in 1685 and is overthrown by William of Orange's invasion in 1688 ([[william-iii]]). His French alignment, inherited from the restoration, is why the Navy and the establishment are slow to defend him."],
  open_q=[])
D("william-iii", "canon", sum="Stadholder who takes the English crown by force of arms in 1688–89.",
  body=["Canon says a conservative, French-aligned monarchy ends in union under a Dutch dynasty around 1688–89. It comes by invasion, not by invitation or inheritance: William lands with a Dutch army and fleet and the Navy's allegiance decides it ([[james-ii]]). The crown he takes unites the House of Orange to the Cranmerian Communion's senior kingdom."],
  open_q=[])
D("prince-rupert", body=["Rupert was born in December 1619, just after [[frederick-v]] was elected king of Bohemia. In history he commanded Charles I's cavalry. In this timeline he is the cavalry general of the Royalist cause, nephew and champion of Charles II ([[charles-ii]]), against Cromwell's troopers ([[oliver-cromwell]])."],
  open_q=[])
D("edgehill", sum="Indecisive first battle of the English War.", open_q=[])
D("lansdown", sum="Royalist victory in the west in which Grenville falls.")
D("marston-moor", sum="Victory of the Reforming Crown's army in the north.")
D("naseby", sum="Royalist victory after which Charles I is deposed.",
  body=["The Royalists, with Rupert's cavalry, break the Reforming Crown's army in Northamptonshire in June 1645. The king is deposed and goes into exile, and the Royalists proclaim his son ([[charles-ii]])."],
  open_q=[])
fact("naseby", "Result", "Royalist victory; Charles I deposed")
D("preston-1648", sum="Victory of the Reforming Crown's army over the Royalists' northern invasion.",
  body=["In August 1648 Cromwell's army defeats the Royalist and Scottish invasion at Preston ([[oliver-cromwell]]). The Reforming party holds the country until the restoration of 1660."])
D("oliver-cromwell", sum="Cavalry commander of the Reforming Crown, victor at Marston Moor and Preston.",
  body=["Cromwell made his name fighting the king in history. Here he fights for the reforming party: the army and Commons against the bishops, the lords and the Navy. After Preston he is the strongest soldier in a country with no king on the throne until 1660."],
  open_q=["Whether Cromwell holds a title (Lord Protector or similar) between 1649 and 1660."])
D("laud", sum="Bishop of London, chief of the Royalist establishment, who opposes the king.",
  body=["In history Laud was Archbishop of Canterbury from 1633 and was executed in 1645. Here the king favours a low-church settlement and Canterbury is left vacant after Abbot's death in 1633, a symptom of the quarrel. Laud, as Bishop of London, is the establishment's leader in everything but title."],
  open_q=[])
D("george-abbot", "canon", body=["Abbot led a low-church, Reformed-friendly bench in history. Here his death in 1633 leaves Canterbury, the Communion's senior see, vacant at the 1635 snapshot, and the establishment cannot elect Laud against the king ([[laud]])."])
D("john-cosin", body=["In our history Cosin was a high-church Caroline bishop of Durham who held that Christ is truly present because of the consecration, and who rejected both transubstantiation and the view that the presence exists only in the receiving. This timeline gives his teaching to the Communion. The [[lambeth-formula]] says Christ is present spiritually, through the Spirit and the consecration, and the benefit is by faith.",
  "Cosin was born in 1595, so he cannot have written the 1552 formula. He is its great exposition, the figure whose books make the compromise respectable to the English clergy and to Hemmingsen's Denmark. In the English War he stands with the Royalist establishment and the Byzantinist circle ([[byzantinists]]). The hardline Reformed hold that presence comes only to the believing receiver, and that is why they refuse the united front ([[hardline-reformed]])."],
  open_q=["Whether the formula is Lambeth's own text or Cosin's later gloss on it."])

# ------------------------------------------------------------------ France
for i, res in [("dreux", "Royal and Guise victory; Condé captured"), ("jarnac-moncontour", "Royal victories"),
               ("coutras", "Navarre's victory"), ("ivry", "Henry IV's victory")]:
    D(i, "canon", open_q=[])
    _by[i]["facts"][-1][1] = res
D("dreux", sum="The first pitched battle of the French wars of religion, won by the royal and Guise army.",
  body=["Poissy ([[poissy]]) opens a framework but does not end the fighting. The Guise party ([[guise-party]]) breaks the peace, and the royal army wins at Dreux, as in history. The settlement waits until the wars are spent and is ratified around 1576–77."])
D("jarnac-moncontour", sum="Royal victories in the third French war.",
  body=["The Crown wins both battles, as in history, but Coligny ([[coligny]]) escapes with the Huguenot army and keeps the moderates together."])
D("coutras", sum="Navarre's cavalry victory over the royal army.",
  body=["Henry of Navarre wins the first Huguenot battlefield victory, as in history ([[henry-iv]]). He is a Cranmerian-leaning Huguenot and the heir to the throne."])
D("ivry", sum="Henry IV's victory over the Catholic League.",
  body=["Henry IV defeats the League army ([[catholic-league]]), as in history, and the succession crisis of 1589 is settled on the field."])
D("coligny", "canon", sum="Admiral of France and leader of the moderate Huguenots, who survives the wars.",
  body=["The wars of religion happen here, but there is no St Bartholomew's massacre, so Coligny lives. He leads the Cranmerian Huguenots into the Gallican–Augustinian settlement, ratified around 1576–77."],
  open_q=["How long Coligny lives."])
D("poissy", open_q=["What carries Poissy through the later wars despite Tournon.", "The exact ratification date."])

# ------------------------------------------------------------------ Dutch quarrel
D("synod-of-dort", "canon", sum="The Dutch synod that condemns the Remonstrants, as in history.",
  body=["Gomarus ([[gomarus]]) and the strict party prevail over the followers of Arminius ([[arminius]]). The Remonstrants ([[remonstrants]]) are condemned and Oldenbarnevelt ([[oldenbarnevelt]]) is executed in 1619, with Maurice of Nassau ([[maurice-of-nassau]]) behind the verdict. Grotius ([[grotius]]) is imprisoned. The Dutch church's strictness here sits uneasily with the wider formula of Lambeth ([[lambeth-formula]]), which the Hemmingsen line prefers."],
  open_q=[])
fact("synod-of-dort", "Effect", "Remonstrants condemned; Oldenbarnevelt executed")
D("remonstrants", "canon", sum="The Dutch party of wider grace around Arminius, condemned at Dort.", open_q=[])
D("oldenbarnevelt", "hist", sum="Advocate of Holland, executed in 1619.", open_q=[], body=["Oldenbarnevelt backs the Remonstrants and loses to Maurice. He is executed in 1619 after the Synod of Dort ([[synod-of-dort]])."])
D("arminius", "hist", open_q=[]); D("gomarus", "hist")

# ------------------------------------------------------------------ Rome and the Empire
D("gian-pietro-carafa", "canon", body=["Carafa leads the hard-line Zelanti ([[zelanti]]). He is elected pope as Paul IV in 1555, as in history, but his Trent is the softened one and the decrees bind him. His is a hard reign inside narrow limits."], open_q=[])
D("peace-1648", "canon", sum="The settlement that ends the great war, recognising Roman and Gnesio-Catholic churches in the Empire, with Lyon a guarantor.",
  body=["Canon records Lyon as a guarantor of the peace. The Empire recognises two confessions: the Roman and the Gnesio-Catholic. The Cranmerian Communion's princes shelter under the Augsburg Confession, and the Reformed hardliners and the Anabaptists are tolerated only."],
  open_q=["What normative year applies."])
fact("peace-1648", "Effect", "Roman and Gnesio-Catholic recognised; Lyon a guarantor")
D("johann-gerhard", "canon", open_q=[]); D("jonas-bretkunas", "canon", open_q=[])
D("martin-chemnitz", "prop", body=["Chemnitz was a pillar of the Lutheran confession in Brunswick. In this timeline Trent's Session 6 allows imputed righteousness, so his Examination of the Council of Trent is a different book: it turns on the Mass, the sacraments and primacy, not on justification. He holds no office beyond his pastorate."], open_q=[])

# ------------------------------------------------------------------ Russia and Sweden
D("peter-i", "canon", sum="Tsar who replaces the patriarchate with the Holy Synod in 1721.",
  body=["Peter I abolishes the patriarchate in 1721 and puts the church under a Holy Synod, as in history. Here it is the church of Filaret's catechism ([[filaret-catechism]]), and his churchman is Prokopovich ([[feofan-prokopovich]])."], open_q=[])
D("feofan-prokopovich", "canon", body=["Prokopovich drafts the Spiritual Regulation of 1721 for the Holy Synod ([[peter-i]]) and defends the catechism's dual imputation against the Kievan critics ([[kiev-resisters]])."], open_q=[])
D("christina-of-sweden", "canon", sum="Queen of Sweden who abdicates in 1654 and stays Gnesio-Catholic.",
  body=["Christina reigns from 1632 and abdicates in 1654 in favour of her cousin Charles X Gustav, as in history. In this timeline she does not convert to Rome."], open_q=[])

# ------------------------------------------------------------------ Scientists
D("galileo", "canon", sum="Pisan astronomer tried by the Roman Inquisition in 1633.",
  body=["Urban VIII's court condemns Galileo in 1633 ([[urban-viii]]), as in history. A softer Trent does not change the Inquisition's natural philosophy."], open_q=[])
D("kepler", "canon", body=["Kepler's laws appear in 1609. In history his Lutheran church excommunicated him over the Eucharist. Under the Lambeth formula ([[lambeth-formula]]) his sacramental views fit inside the Communion, so he is not excommunicated."], open_q=[])

# ------------------------------------------------------------------ Narva, Zizanius, Bossuet, Jerusalem
P("johannes-matthiae", "Johannes Matthiae", "leader", "prop", "1592–1670", 1635,
  "Swedish irenicist and tutor of Christina, proposed as the Orthodox primate at Narva.",
  ["In history Matthiae was a Swedish bishop (Strängnäs, from 1643), tutor to Queen Christina and the most famous Swedish irenicist, who wrote for reunion among the Christian churches and was accused of too soft a line on Rome. Here he is the primate of the Western-Rite church at Narva ([[western-rite-orthodox]]): a Swede trained in the Gnesio-Catholic church who takes Orthodox chrismation, the natural bridge between Uppsala and Moscow in the Narva treaty ([[stolbovo]]). Christina ([[christina-of-sweden]]) is his pupil."],
  ["western-rite-orthodox", "gnesio-orthodox"], "Primate of Narva", "Johannes Matthiae", y2=1670,
  open_q=["Whether the primate of 1600 and the primate of 1635 are the same man; Matthiae was only eight in 1600."])
D("western-rite-orthodox", open_q=["Who holds the primacy between about 1600 and Matthiae's appointment."], add_faith=[])
D("lavrentiy-zizanius", "canon", sum="Ruthenian catechist whose Vilnius catechism is a source for Filaret's.",
  body=["In our history Zizanius published a Great Catechism at Vilnius in 1627, which Patriarch Filaret condemned in Moscow. In this timeline the traffic goes the other way: his Kiev-educated Gnesio-influenced formulas are a source that Filaret's drafters use, but he does not draft the catechism himself ([[filaret-catechism]]). It makes the catechism a Muscovite text with a Ruthenian source."],
  open_q=[])
D("bossuet", "canon", sum="Bishop of Meaux, drafter of the Gallican declaration of 1682 and later the Gallican Church's catechist.",
  body=["Bossuet drafts the declaration of 1682 ([[gallican-articles-1682]]), which only restates the settlement already in force under Lyon's primacy. In later life he becomes more sympathetic to a high view of the papacy.",
        "In his Catechism of the Gallican Church ([[gallican-catechism]]) he teaches that the conciliarist canons of Constance and Basel are authoritative because of the pope, whose confirmation gives them force. The line is controversial: Gallican conciliarists read it as a surrender, and the Curia reads it as a concession of principle. It sets a trend, moving Gallican theology toward papal confirmation as the source of conciliar authority."])
D("gallican-articles-1682", "canon", sum="The French clergy restate the existing Gallican settlement.",
  body=["Bossuet ([[bossuet]]) drafts the four articles for Louis XIV ([[louis-xiv]]). Because the Lyon primacy and the 1516 concordat ([[concordat-of-bologna]]) already fix the balance, they add nothing new: they restate the settlement."])
D("synod-of-jerusalem-1672", "canon", sum="The Greek counterpart to Trent or Florence: a reform council that reaches agreement with the Armenian Church.",
  body=["Dositheos of Jerusalem ([[dositheos-of-jerusalem]]) convenes the synod as the Greek world's answer to Trent and Florence, in importance if not in size. Its aim is to compete with the Russians, whose catechism ([[filaret-catechism]]) has split Moscow from the Greeks doctrinally, and eventually to influence them. It condemns the Russian formulas and the Calvinising confession tradition of Lucaris ([[cyril-lucaris]], [[peter-mohyla]]) without breaking communion with Moscow.",
        "Its reforms cover the liturgy, the seminaries and the clergy. The Greek rite is revised and printed from a corrected text. Seminaries are reformed on a model that borrows from both sides: Byzantine teachers and Roman Catholic help, as with the Greek College in Rome, and the Kievan scholastic method that Moscow has taken in after Pereiaslav ([[pereiaslav]]). Graduates are meant to staff the Greek, Serbian and Ruthenian churches and to argue with Moscow on its own ground.",
        "The agreement with the Armenian Church is its largest act. The Greeks accept the Cyrilline formula, 'one incarnate nature of God the Word', as compatible with Chalcedon, and the Armenians accept that Chalcedon's two natures were not Nestorian. Catholicos Hakob IV of Julfa ([[hakob-iv-julfa]]) signs for Etchmiadzin, with the Armenian scholars of Constantinople and the printers of Amsterdam ([[voskan-yerevantsi]]). The Armenians keep their liturgy, calendar and episcopal order, and their trade diaspora in Venice, Isfahan, Lviv and Astrakhan carries the reforms into the Russian and Polish-Lithuanian world ([[miaphysite]])."],
  open_q=["How the Armenian Patriarchate of Constantinople and the Catholicate of Etchmiadzin divide authority after the agreement.", "Whether the Copts and the Syriac patriarchate follow later, as a partial agreement."])
fact("synod-of-jerusalem-1672", "Parties", "Greek patriarchates and the Armenian Church")
fact("synod-of-jerusalem-1672", "Effect", "Liturgy and seminary reform; agreement with the Armenians")
D("synod-of-jerusalem-1672", add_faith=["miaphysite"])

P("dositheos-of-jerusalem", "Dositheos II of Jerusalem", "leader", "hist", "1641–1707", 1672,
  "Patriarch of Jerusalem, who presided over the Synod of Jerusalem in 1672.",
  ["In history Dositheos' synod condemned the Calvinising confession attributed to Lucaris. Here the same synod widens its work to the Russian catechism and to an agreement with a miaphysite church ([[synod-of-jerusalem-1672]])."],
  ["eastern-orthodox"], "Patriarch of Jerusalem", "Dositheos II of Jerusalem", y2=1707)

from common import E
E("gallican-catechism", "doc", "Catechism of the Gallican Church", "canon", "1690s", 1695,
  "Bossuet's catechism, which says the conciliarist canons of Constance and Basel are authoritative because of the pope.",
  ["Written late in Bossuet's life ([[bossuet]]), the catechism teaches the Gallican liberties from a higher view of the papacy than the articles of 1682 ([[gallican-articles-1682]]). Its disputed line is that the canons of Constance and Basel bind because the pope confirms them. Conciliarists object that this makes the pope the source of conciliar authority. The Curia objects that it concedes a conciliar principle at all. The Gallican Church receives the catechism, and its trend toward papal confirmation outlasts him."],
  facts=[["Date", "1690s"], ["Kind", "Catechism"], ["Parties", "Bossuet and the French clergy"], ["Effect", "Gallican theology moves toward papal confirmation of councils"]],
  faith=["gallican-church"])

P("hakob-iv-julfa", "Hakob IV of Julfa", "leader", "prop", "d. 1680", 1672,
  "Catholicos of All Armenians at Etchmiadzin 1655–80.",
  ["In history Hakob IV was Catholicos from 1655 and encouraged Armenian printing. Here he signs the agreement with the Greek patriarchates at the Synod of Jerusalem in 1672 ([[synod-of-jerusalem-1672]]), a role history did not give him."],
  ["miaphysite"], "Catholicos of Etchmiadzin", "Hakob IV of Julfa", y2=1680)
P("voskan-yerevantsi", "Voskan Yerevantsi", "scholar", "hist", "1614–74", 1666,
  "Armenian bishop and printer who published the first printed Armenian Bible at Amsterdam in 1666.",
  ["Voskan's press at Amsterdam gives the Armenians a printing tradition the Greeks lack. In this timeline his printing is what the Jerusalem agreement ([[synod-of-jerusalem-1672]]) builds on for the corrected texts and seminary books."],
  ["miaphysite"], "Bishop and printer", "Voskan Yerevantsi", y2=1674)
