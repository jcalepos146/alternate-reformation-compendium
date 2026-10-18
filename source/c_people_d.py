from common import P

def A(id, name, when, y, sum, body, faith, office, wiki, y2=None, role="artist", st="hist", open_q=None):
    P(id, name, role, st, when, y, sum, [body] if isinstance(body, str) else body, faith, office, wiki, y2=y2, open_q=open_q)

# ----------------------------------------------------------------- Painters, sculptors, architects
A("leonardo", "Leonardo da Vinci", "1452–1519", 1500, "Painter, engineer and anatomist.",
  "Leonardo works in Milan, Florence and, after Marignano ([[marignano]]), in the service of Francis I. He dies in 1519.",
  ["roman-catholic"], "Painter and engineer", "Leonardo da Vinci", y2=1519)
A("raphael", "Raphael", "1483–1520", 1508, "Painter of the Vatican Stanze for Julius II and Leo X.",
  "Raphael works for [[julius-ii]] and [[leo-x]] and dies young in 1520, before any evangelical movement has altered Rome's patronage.",
  ["roman-catholic"], "Painter", "Raphael", y2=1520)
A("michelangelo", "Michelangelo", "1475–1564", 1508, "Sculptor, painter and architect of the Sistine ceiling and the Last Judgment.",
  "Michelangelo painted the ceiling for Julius II. His circle around Vittoria Colonna overlaps with the Spirituali ([[spirituali]], [[reginald-pole]]), who in this timeline win at Trent ([[council-of-trent]]).",
  ["roman-catholic"], "Artist", "Michelangelo", y2=1564)
A("titian", "Titian", "c.1488–1576", 1530, "Venetian painter to Charles V and Philip II.",
  "Titian paints [[charles-v]] after Mühlberg ([[muhlberg]]), Paul III ([[paul-iii]]) and Philip II ([[philip-ii]]).",
  ["roman-catholic"], "Painter", "Titian", y2=1576)
A("tintoretto", "Tintoretto", "1518–94", 1560, "Venetian painter of enormous religious cycles.",
  "Working in the republic of Venice that defied the pope in 1606 ([[venetian-interdict]]), he dies a decade before it.",
  ["roman-catholic"], "Painter", "Tintoretto", y2=1594)
A("el-greco", "El Greco", "1541–1614", 1577, "Cretan painter trained in the Byzantine icon tradition, working in Toledo.",
  "He bridges the Orthodox and Roman worlds. His Toledo is in Spain under Philip II ([[philip-ii]]), but his training is in Candia, Venetian Crete.",
  ["roman-catholic", "eastern-orthodox"], "Painter", "El Greco", y2=1614)
A("caravaggio", "Caravaggio", "1571–1610", 1600, "Painter whose Roman altarpieces broke with convention.",
  "Caravaggio's career in the Rome of Clement VIII and Paul V runs as in history, and ends in 1610.",
  ["roman-catholic"], "Painter", "Caravaggio", y2=1610)
A("durer", "Albrecht Dürer", "1471–1528", 1511, "Nuremberg printmaker and painter, a supporter of Luther.",
  "Dürer wrote in his diary of Luther's capture in 1521. He dies in 1528, so his Nuremberg is a city of the Philippists in the Cranmerian communion ([[cranmerian]]).",
  ["gnesio-catholic", "cranmerian"], "Painter and printmaker", "Albrecht Dürer", y2=1528)
A("cranach", "Lucas Cranach the Elder", "1472–1553", 1520, "Wittenberg court painter, the face of Luther's reformation.",
  "Cranach painted [[martin-luther]], [[melanchthon]] and [[frederick-the-wise]]. He followed John Frederick into captivity after Mühlberg ([[muhlberg]]), and died in Weimar.",
  ["gnesio-catholic", "cranmerian"], "Court painter", "Lucas Cranach the Elder", y2=1553)
A("holbein", "Hans Holbein the Younger", "c.1497–1543", 1527, "German painter at the courts of Henry VIII.",
  "Holbein painted [[erasmus]], [[thomas-more]], [[thomas-cromwell]] and [[henry-viii]]. His likeness of Henry is the standard image of the king.",
  ["cranmerian"], "Court painter", "Hans Holbein the Younger", y2=1543)
A("bruegel", "Pieter Bruegel the Elder", "c.1525–69", 1559, "Flemish painter of peasants and proverbs.",
  "Bruegel died in 1569, just after the Netherlands revolt began ([[dutch-revolt]]). His Antwerp and Brussels lie in the southern provinces that Spain retakes.",
  ["roman-catholic"], "Painter", "Pieter Bruegel the Elder", y2=1569)
A("rubens", "Peter Paul Rubens", "1577–1640", 1610, "Antwerp painter and diplomat.",
  "Rubens works for the Spanish Netherlands after the fall of Antwerp ([[fall-of-antwerp]]) and travels as an envoy between Madrid and London.",
  ["roman-catholic"], "Painter and diplomat", "Peter Paul Rubens", y2=1640)
A("van-dyck", "Anthony van Dyck", "1599–1641", 1632, "Flemish painter at the court of Charles I.",
  "Van Dyck paints the king. In this timeline [[charles-i-england]] is the reforming king, which changes the symbolism of the portraits rather than their painter.",
  ["cranmerian"], "Court painter", "Anthony van Dyck", y2=1641)
A("rembrandt", "Rembrandt", "1606–69", 1642, "Dutch painter of Amsterdam.",
  "Rembrandt lives in the Cranmerian republic of the United Provinces, where Mennonites and Remonstrants ([[remonstrants]]) were among his patrons.",
  ["cranmerian"], "Painter", "Rembrandt", y2=1669)
A("velazquez", "Diego Velázquez", "1599–1660", 1634, "Painter to Philip IV.",
  "Velázquez records the court of [[philip-iv]], with [[olivares]] as chief minister.",
  ["roman-catholic"], "Court painter", "Diego Velázquez", y2=1660)
A("simon-ushakov", "Simon Ushakov", "1626–86", 1664, "Moscow icon painter whose style absorbed Western techniques.",
  "Ushakov's icons use shading and perspective learned from Kievan and Western prints, a pattern in the same Moscow that absorbs the Kievan scholars after Pereiaslav ([[pereiaslav]]).",
  ["russian-orthodox"], "Icon painter", "Simon Ushakov", y2=1686)
A("inigo-jones", "Inigo Jones", "1573–1652", 1616, "Architect of the Stuart court.",
  "Jones's Queen's House and Banqueting House were built for James and Charles ([[james-vi-i]], [[charles-i-england]]). His classical taste is closer to the Byzantinist circle than to the Royalist establishment ([[byzantinists]]).",
  ["cranmerian"], "Architect", "Inigo Jones", y2=1652)

# ----------------------------------------------------------------- Composers
A("palestrina", "Giovanni Pierluigi da Palestrina", "c.1525–94", 1562, "Roman composer of polyphonic Masses.",
  "Palestrina's style is held to have answered the reforming demands of Trent ([[council-of-trent]]). In this timeline Trent is softer, but the demand for intelligible text remains.",
  ["roman-catholic"], "Composer", "Giovanni Pierluigi da Palestrina", y2=1594)
A("lassus", "Orlande de Lassus", "1532–94", 1563, "Franco-Flemish composer at the Bavarian court.",
  "Lassus directs the Munich chapel under Duke Albert V.",
  ["roman-catholic"], "Composer", "Orlande de Lassus", y2=1594)
A("tallis", "Thomas Tallis", "c.1505–85", 1549, "English composer who served four monarchs.",
  "Tallis wrote for the Latin rite and for the new English liturgy ([[book-of-common-prayer]]) in the same career.",
  ["cranmerian"], "Composer", "Thomas Tallis", y2=1585)
A("schutz", "Heinrich Schütz", "1585–1672", 1617, "Dresden Kapellmeister, the greatest German composer of his century.",
  "Schütz serves [[john-george-i]] in Albertine Saxony, a Philippist court in the Cranmerian communion, through the war years ([[lutzen]]).",
  ["cranmerian"], "Composer", "Heinrich Schütz", y2=1672)
A("monteverdi", "Claudio Monteverdi", "1567–1643", 1613, "Composer at Mantua and Venice.",
  "Monteverdi becomes maestro di cappella at San Marco in 1613, in the republic that faced the pope in 1606 ([[venetian-interdict]]).",
  ["roman-catholic"], "Composer", "Claudio Monteverdi", y2=1643)

# ----------------------------------------------------------------- Scholars and scientists
A("copernicus", "Nicolaus Copernicus", "1473–1543", 1543, "Canon of Frombork and author of De revolutionibus.",
  "His book appears in 1543, in the Prussian bishopric of Ermland, Roman and under the Polish crown, while the Wittenberg circle ([[melanchthon]]) debates it.",
  ["roman-catholic"], "Astronomer and canon", "Nicolaus Copernicus", y2=1543, role="scholar")
A("tycho-brahe", "Tycho Brahe", "1546–1601", 1576, "Danish astronomer at Hven and Prague.",
  "Tycho observes under Frederick II of Denmark and then under [[rudolf-ii]] at Prague.",
  ["cranmerian"], "Astronomer", "Tycho Brahe", y2=1601, role="scholar")
A("kepler", "Johannes Kepler", "1571–1630", 1609, "Mathematician and astronomer of Prague and Linz.",
  "Kepler's laws appear in 1609. In history his Lutheran church excommunicated him over the Eucharist. Under the Lambeth formula ([[lambeth-formula]]) his sacramental views might fit inside the Communion, which is an open question.",
  ["cranmerian"], "Mathematician and astronomer", "Johannes Kepler", y2=1630, role="scholar", st="prop",
  open_q=["Whether Kepler is excommunicated here."])
A("galileo", "Galileo Galilei", "1564–1642", 1633, "Pisan astronomer tried by the Roman Inquisition.",
  "In history Urban VIII's court condemned Galileo in 1633 ([[urban-viii]]). In this timeline the Spirituali's softer Rome ([[spirituali]]) may or may not extend to natural philosophy.",
  ["roman-catholic"], "Astronomer and physicist", "Galileo Galilei", y2=1642, role="scholar", st="prop",
  open_q=["Whether the trial occurs in a softer Rome."])
A("mercator", "Gerardus Mercator", "1512–94", 1569, "Cartographer of Duisburg.",
  "Mercator's projection of 1569 is made in Cleves, the duchy that [[xanten]] later assigns to Brandenburg.",
  ["cranmerian"], "Cartographer", "Gerardus Mercator", y2=1594, role="scholar")
A("plantin", "Christophe Plantin", "c.1520–89", 1568, "Antwerp printer of the Polyglot Bible.",
  "Plantin prints for Philip II ([[philip-ii]]) in a city that Farnese retakes in 1585 ([[fall-of-antwerp]]).",
  ["roman-catholic"], "Printer", "Christophe Plantin", y2=1589, role="scholar")
A("grotius", "Hugo Grotius", "1583–1645", 1625, "Dutch jurist and theologian, author of On the Law of War and Peace.",
  "Grotius sided with [[oldenbarnevelt]] and the Remonstrants ([[remonstrants]]) in history, and was jailed after Dort ([[synod-of-dort]]).",
  ["cranmerian"], "Jurist and theologian", "Hugo Grotius", y2=1645, role="scholar")
