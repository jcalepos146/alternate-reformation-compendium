from common import E

# Political and theological parties. "faith" lists the communities each party sits in.

E("philippists", "faction", "Philippists", "canon", "1548–1789", 1548, "Followers of Melanchthon, who yield on ceremonies and win the contest with the Gnesio party.",
  ["After Mühlberg the Wittenberg movement splits over the Interim. The Philippists of Albertine Saxony, Brandenburg, Hesse, Pomerania, Anhalt, Württemberg, Ansbach and Denmark-Norway accept the Leipzig compromise ([[augsburg-interim]]). Because they win, the Gnesio party shrinks to its core.",
   "Their victory is why the larger body is called the Cranmerian–Philippist Communion, and why Mecklenburg, Lüneburg, Hamburg, Lübeck and the Neumark, Gnesio in 1550, sit inside the Communion with Gnesio-Catholic stripes in 1575."],
  faith=["cranmerian"], rel=[["gnesio-lutherans", "The opposing party."]])

E("gnesio-lutherans", "faction", "Gnesio-Lutherans", "canon", "1548–75", 1548, "The hard party of Flacius and Amsdorf that refuses both Interims.",
  ["Strongest in Ernestine Thuringia, Magdeburg, Mansfeld, and the Hanseatic north in 1550. The party becomes the Gnesio-Catholic church at the Bohemian union of 1575 ([[bohemian-union-1575]])."],
  faith=["gnesio-catholic"], rel=[["philippists", "The opposing party."]])

E("spirituali", "faction", "The Spirituali", "canon", "1535–1789", 1541, "A circle of reforming cardinals seeking a settlement with the evangelicals.",
  ["Contarini, Pole and Morone hold the line that justification can be taught in terms both Rome and Wittenberg can accept. In this timeline their argument wins at Trent in 1547 and the Roman communion becomes more Augustinian."],
  faith=["roman-catholic"])

E("baianists", "faction", "Baianists", "canon", "1567–1789", 1567, "The Augustinian school of Louvain and Ghent.",
  ["Followers of Baius teach that fallen human nature cannot do good without grace. Rome censures them only lightly and Spanish authorities tolerate them. Friction with Lyon’s catechism on concupiscence is an open question. Jansen is a proposed successor."],
  faith=["roman-catholic", "gallican-church"],
  open_q=["How Baius’s teaching on concupiscence squares with Lyon’s catechism."])

E("guise-party", "faction", "The Guise Party and the Holy League", "hist", "1560–1598", 1576, "The ultra-Catholic faction of the Guise family and the League.",
  ["The Guises hold Reims and press their own primatial claims. The Catholic League problem and the succession in 1589, when the Protestant Henry of Navarre was heir, survive in this timeline even with shorter wars and a partly successful Poissy."],
  faith=["roman-catholic"])

E("parlement-paris", "faction", "The Parlement of Paris", "hist", "to 1789", 1500, "The court that guards Gallican liberties against churchmen.",
  ["The Parlement is a resistance point to Lyon’s primacy. It refuses any churchman a claim over the Crown’s church. Its alliance with the king is what makes the Gallican settlement work."],
  faith=["gallican-church"])

E("huguenot-hardliners", "faction", "Hardline Huguenots", "canon", "to 1628", 1561, "Huguenots of Béarn, Languedoc and La Rochelle.",
  ["Strict Calvinists who refuse the Cranmerian settlement. Broken at [[la-rochelle]] in 1628, they shrink to the Cévennes and Béarn’s mountains."],
  faith=["hardline-reformed"])

E("huguenot-moderates", "faction", "Cranmerian Huguenots", "canon", "1561–1789", 1561, "Moderate Huguenots of Normandy, Poitou and Dauphiné who join the Cranmerian communion.",
  ["Protected by Henry IV’s edict and not revoked. In 1685 they are still protected."],
  faith=["cranmerian"])

E("reconciled-huguenots", "faction", "Reconciled Huguenots", "canon", "1561–1789", 1561, "Nobles and townspeople around Paris, Orléans and Lyon who return to the Gallican church.",
  ["A substantial group, mostly elites, reconciles with Lyon. More individuals reconcile than in history."],
  faith=["gallican-church"])

E("catholic-league", "faction", "The Catholic League", "canon", "1609–1635", 1609, "The Bavarian-led bloc of Roman Catholic princes in the Empire.",
  ["One of the armed blocs on the eve of 1618. Under Maximilian of Bavaria, it fights the Bohemian revolt and the Palatinate."],
  faith=["roman-catholic"])

E("evangelical-union", "faction", "The Cranmerian Union", "canon", "1608–1635", 1608, "The Palatinate-led bloc of Cranmerian princes.",
  ["Another armed bloc on the eve of the war. It backs Frederick V and collapses when Saxony and Brandenburg make peace at Prague in 1635 ([[peace-of-prague]])."],
  faith=["cranmerian"])

E("bohemian-estates", "faction", "The Bohemian Estates", "canon", "1609–1620", 1609, "The nobles and towns who defy the Habsburgs in 1618.",
  ["Gnesio-Catholic in confession, with the Brethren as allies. They depose Ferdinand and elect Frederick V in 1619 ([[defenestration-1618]]). After [[white-mountain]] the moderates make terms with Rome and the hardliners flee."],
  faith=["gnesio-catholic", "unity-brethren"])

E("royalists", "faction", "The Royalists (the establishment)", "canon", "1640s–1660s", 1640, "The Church of England’s bishops, the nobility and the Navy, who fight in the king’s name against his ministers and then back a rival Stuart.",
  ["The Royalists lean toward the old constitution and the episcopal establishment. The war comes in two stages: first they fight for the king against his reforming ministers, then, once the king openly sides with the Commons, they back a rival Stuart. Canon records a Royalist restoration by 1660 and a conservative, French-aligned monarchy afterward."],
  faith=["cranmerian"], rel=[["byzantinists", "A smaller, more radical party on the same side."], ["reforming-crown", "The opposing party."]])

E("reforming-crown", "faction", "The Reforming Crown", "canon", "1620s–1640s", 1635, "The king and his ministers, backed by Commons.",
  ["The crown favours a low-church, more democratic Church of England and economic liberalisation. It is the revolutionary party in this timeline: the roles of 1642 are reversed."],
  faith=["cranmerian"], rel=[["royalists", "The opposing party."]],
  open_q=["How the crown fares in the war; canon records a Royalist restoration."])

E("polish-toleration-party", "faction", "The Polish Toleration Party", "canon", "1573–1789", 1573, "The nobles who defend the Warsaw Confederation against Jesuit pressure.",
  ["The twist in this timeline is legal recognition of Gnesio-Catholic congregations. Toleration survives the Deluge and Kaunas emerges stronger. The main threat is Sigismund III and the Jesuits."],
  faith=["gnesio-independent"])

E("filaret-party", "faction", "The Anti-Latin Party in Moscow", "canon", "1612–1685", 1620, "Filaret’s circle and the clergy who adopt Gnesio formulas against Rome.",
  ["After the Polish occupation, anti-Latin feeling makes Lutheran categories an acceptable weapon. The party drives [[filaret-catechism]] and is split afterward over how far dual imputation may go."],
  faith=["russian-orthodox"])

E("kiev-resisters", "faction", "The Kievan Resisters", "canon", "1627–1700", 1627, "Kiev-trained clergy and monastic circles who resist the catechism.",
  ["Under [[peter-mohyla]] they stand for the Greek formulas and Constantinople. After Pereiaslav ([[pereiaslav]]) Moscow absorbs its main critics, and they become an opposition inside the Russian church that later breaks away. They are the timeline’s equivalent of the Old Believers."],
  faith=["eastern-orthodox", "russian-orthodox"])

E("cossacks", "faction", "The Zaporozhian Cossacks", "canon", "1648–1700", 1648, "The host whose rising of 1648 leads to union with Moscow in 1654.",
  ["The rising of Khmelnytsky happens as in history. Pereiaslav still follows, and Kiev’s resisters are folded into Moscow’s world."],
  faith=["eastern-orthodox"])

E("west-country-reactionaries", "faction", "The West Country Reactionaries", "canon", "1630s–1650s", 1630, "The English party that wants autocracy on Roman and Byzantine models.",
  ["Strongest in Devon, Cornwall, Bristol and Exeter. They want an autocratic monarchy, a modernised army and a church closer to the Greeks. See [[byzantinists]]."],
  faith=["byzantinists"])
