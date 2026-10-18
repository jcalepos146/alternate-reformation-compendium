from c_docs import D
from common import E

# ============================================================ Documents
D("ninety-five-theses", "The Ninety-Five Theses", "hist", "31 October 1517", 1517,
  "Luther's challenge to the sale of indulgences.",
  ["Marignano ([[marignano]]) happened two years earlier and touches Zurich, not Wittenberg, so the theses appear as in history ([[martin-luther]])."],
  "Luther and the Archbishop of Mainz", "Opens the Wittenberg reformation", faith=["gnesio-catholic"], kind="Disputation")
D("diet-of-worms", "Diet of Worms", "hist", "1521", 1521,
  "Luther refuses to recant before Charles V.",
  ["Frederick the Wise ([[frederick-the-wise]]) shelters Luther at the Wartburg after the edict."],
  "Charles V, Luther, the princes", "Edict of Worms; Luther outlawed", faith=["gnesio-catholic", "roman-catholic"], kind="Diet")
D("augsburg-confession", "Augsburg Confession", "hist", "1530", 1530,
  "Melanchthon's confession presented to Charles V.",
  ["The text is later claimed by Philippists and Gnesio-Catholics alike, which is the question the Peace of Augsburg left open ([[peace-of-augsburg]])."],
  "Evangelical princes and cities", "Foundational evangelical confession", faith=["cranmerian", "gnesio-catholic"], kind="Confession")
D("act-of-supremacy", "Act of Supremacy", "hist", "1534", 1534,
  "The English king becomes head of the English church.",
  ["Thomas Cromwell ([[thomas-cromwell]]) carries it through Parliament. The break with Rome comes before the doctrinal change, which is Cranmer's work."],
  "Henry VIII and Parliament", "Royal supremacy", faith=["cranmerian"], kind="Statute")
D("schmalkaldic-articles", "Schmalkaldic Articles", "hist", "1537", 1537,
  "Luther's statement for the League and for a possible council.",
  ["The articles draw the line the Gnesio party later holds. They are overtaken by the war ([[schmalkaldic-war]])."],
  "Luther and the League", "Gnesio reference text", faith=["gnesio-catholic"], kind="Confession")
D("book-of-common-prayer", "Book of Common Prayer", "hist", "1549 and 1552", 1549,
  "Cranmer's liturgy in English.",
  ["The 1552 revision carries the eucharistic wording that Lambeth turns into the agreed formula ([[lambeth-formula]])."],
  "Cranmer", "Common liturgy of the Communion", faith=["cranmerian"], kind="Liturgy")
D("stoglav", "Stoglav Council", "hist", "1551", 1551,
  "Moscow's council of a hundred chapters.",
  ["Ivan IV ([[ivan-iv]]) fixes ritual and clergy discipline. It sets the baseline for the later catechism quarrel ([[filaret-catechism]])."],
  "Ivan IV and the Russian church", "Ritual and clergy rules", faith=["russian-orthodox"], kind="Council")
D("peace-of-passau", "Peace of Passau", "hist", "1552", 1552,
  "The agreement that ends the Interim.",
  ["Maurice of Saxony turns on the Emperor ([[maurice-of-saxony]]), if he does so here after such a victory. It is open."],
  "Maurice, Ferdinand, the princes", "Interim lapses; leads to Augsburg", faith=["cranmerian", "gnesio-catholic"],
  open_q=["Whether Maurice revolts after a complete imperial victory."], kind="Treaty")
D("cateau-cambresis", "Peace of Cateau-Cambrésis", "hist", "1559", 1559,
  "Settlement ending the Italian Wars.",
  ["Spain keeps Milan and Naples, and France gives up its Italian claims ([[henry-ii-france]], [[philip-ii]])."],
  "France, Spain, England", "End of the Italian Wars", faith=["roman-catholic"], kind="Treaty")
D("heidelberg-catechism", "Heidelberg Catechism", "hist", "1563", 1563,
  "The Palatine catechism by Ursinus and Olevian.",
  ["Commissioned by [[frederick-iii-palatine]] and written by [[zacharias-ursinus]]. In this timeline it is the Reformed wing's standard, read inside the Communion with the Lambeth formula ([[lambeth-formula]]) as a limit."],
  "Palatine church", "Reformed catechism in the Communion", faith=["cranmerian"], kind="Catechism")
D("union-of-utrecht", "Union of Utrecht", "hist", "1579", 1579,
  "The northern provinces form a federation.",
  ["The union is the base of the Cranmerian republic ([[dutch-revolt]])."],
  "Holland, Zeeland, Utrecht, Groningen, Gelderland", "United Provinces", faith=["cranmerian"], kind="Treaty")
D("venetian-interdict", "Venetian Interdict", "hist", "1606–07", 1606,
  "Venice defies a papal interdict.",
  ["Paolo Sarpi ([[paolo-sarpi]]) argues for the republic. The Roman communion tolerates the quarrel, a precedent for the Gallican settlement."],
  "Venice and Paul V", "Papal retreat", faith=["roman-catholic"], kind="Dispute")
D("letter-of-majesty", "Letter of Majesty", "hist", "1609", 1609,
  "Rudolf II's grant of religious freedom to Bohemia.",
  ["Matthias confirms it ([[matthias]]). Its violation leads to the Defenestration ([[defenestration-1618]])."],
  "Rudolf II and the Bohemian estates", "Religious freedom in Bohemia", faith=["unity-brethren", "gnesio-catholic"], kind="Charter")
D("synod-of-dort", "Synod of Dort", "prop", "1618–19", 1618,
  "Proposed: a Dutch quarrel over predestination, as in history.",
  ["Gomarus ([[gomarus]]) against Arminius ([[arminius]]) and the Remonstrants ([[remonstrants]]). In history the strict party won, and Oldenbarnevelt ([[oldenbarnevelt]]) was executed. Whether the Lambeth Communion's broad formula reduces the quarrel is open."],
  "Dutch church and states", "Open", faith=["cranmerian", "hardline-reformed"],
  open_q=["Whether the Arminian dispute occurs inside a broad Communion.", "Who wins."], kind="Synod")
D("edict-of-restitution", "Edict of Restitution", "hist", "1629", 1629,
  "Ferdinand II demands the return of church lands.",
  ["The edict ([[ferdinand-ii]]) sets the north against the Emperor and Sweden lands in 1630."],
  "Ferdinand II", "Church land restitution", faith=["roman-catholic", "gnesio-catholic"], kind="Edict")
D("synod-of-jerusalem-1672", "Synod of Jerusalem", "prop", "1672", 1672,
  "Proposed: Greek synods condemn the Russian formulas without breaking communion.",
  ["Dositheos' real synod condemned Lucaris' Calvinist confession. Here the target is wider, and the Russian catechism of Filaret ([[filaret-catechism]]) is judged by Greek bishops ([[cyril-lucaris]], [[peter-mohyla]])."],
  "Greek patriarchs", "Condemns Russian formulas; communion holds", faith=["eastern-orthodox", "russian-orthodox"], kind="Synod",
  open_q=["Whether Moscow is censured by name."])
D("gallican-articles-1682", "Gallican Articles", "prop", "1682", 1682,
  "Proposed: the French clergy affirm the Crown's rights against Rome.",
  ["Bossuet ([[bossuet]]) drafts the four articles for Louis XIV ([[louis-xiv]]). Here, with Lyon's primacy already settled, they only restate the existing balance."],
  "French clergy and Louis XIV", "Restates Gallican liberties", faith=["gallican-church"], kind="Declaration")
D("karlowitz", "Treaty of Karlowitz", "hist", "1699", 1699,
  "The Ottomans give up Hungary.",
  ["Leopold I ([[leopold-i]]) gains most of Hungary after Zenta ([[zenta]])."],
  "Habsburgs, Poland, Venice, Ottomans", "End of the Great Turkish War", faith=["roman-catholic", "sunni"], kind="Treaty")

# ============================================================ Factions
E("zelanti", "faction", "The Zelanti", "hist", "1540s–1560s", 1555, "The hard-line cardinals who opposed the Spirituali.",
  ["Led by Gian Pietro Carafa ([[gian-pietro-carafa]]), they distrust any compromise on justification. In this timeline they lose at Trent ([[council-of-trent]]) but remain a strong curial party."],
  faith=["roman-catholic"], rel=[["spirituali", "The opposing party."]])
E("jesuits", "faction", "The Jesuits", "hist", "1540–1773", 1540, "The Society founded by Ignatius Loyola.",
  ["Ignatius ([[ignatius-loyola]]), Canisius ([[peter-canisius]]) and Bellarmine ([[robert-bellarmine]]) shape the Roman response. Under a softened Trent the Society argues for the Roman case in Poland, Bohemia and the Rhineland."],
  faith=["roman-catholic"])
E("josephites", "faction", "Josephites and Non-Possessors", "hist", "c.1503–1580s", 1503, "Rival parties in the Russian church over monastic land.",
  ["Joseph Volotsky ([[joseph-volotsky]]) defended monastic property and a strong monarchy. Nil Sorsky ([[nil-sorsky]]) taught that monks should hold no land. The Josephites win in history, and the same tension returns in the quarrel over the catechism."],
  faith=["russian-orthodox"], rel=[["kiev-resisters", "A later quarrel with a similar shape."]])
E("remonstrants", "faction", "The Remonstrants", "prop", "1610–1619", 1610, "Proposed: the Dutch party of wider grace around Arminius.",
  ["In history they were condemned at Dort ([[synod-of-dort]]). In a Communion whose formula allows spiritual presence by consecration, they might be an accepted wing. Whether the quarrel sets them outside is open."],
  faith=["cranmerian"], rel=[["hardline-reformed", "The strict party that opposes them."]],
  open_q=["Whether they are condemned here."])
E("schmalkaldic-league", "faction", "The Schmalkaldic League", "hist", "1531–1547", 1531, "The defensive league of evangelical princes and cities.",
  ["Led by John Frederick of Saxony and Philip of Hesse ([[philip-of-hesse]]). In this timeline the League is wiped out ([[schmalkaldic-war]]), which is why its survivors accept Cranmer's council."],
  faith=["cranmerian", "gnesio-catholic"])
