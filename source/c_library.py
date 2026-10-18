"""Library: in-world primary sources and period chronicles. Every text is invented wording, written to fit the canon.
Body lines starting with '> ' are the text itself; other lines are editorial notes."""
from common import E

NOTE = "In-world text: the wording is invented for this timeline and is not a historical quotation."


def T(id, name, kind, when, y, sum, body, author, concerns, faith=None, st="prop", open_q=None):
    E(id, "text", name, st, when, y, sum, [NOTE] + body,
      facts=[["Kind", kind], ["Date", when], ["Author or voice", author], ["Concerns", concerns]],
      faith=faith or [], open_q=open_q, basis="Drafted for the compendium; wording is invented.")


SRC, CHR = "Primary source", "Chronicle or newspaper"

# ================================================================ Primary sources
T("src-lambeth-formula", "The Lambeth Formula, as adopted", SRC, "1552", 1552,
  "The agreed article on the Lord's Supper, in the draft form the council adopts.",
  ["The formula is the eucharistic settlement of the Communion ([[lambeth-formula]], [[lambeth-council]]).",
   "> Of the Supper of the Lord.",
   "> We confess that in the Supper Christ is present, truly and spiritually, by the working of the Holy Spirit, through the prayer of consecration; and that this presence is not made by the faith of him that receiveth, nor unmade by his unbelief.",
   "> We deny that the bread and wine are changed in their substance, as the schools of Rome have taught. We deny also that the body of Christ is in all places, or is received with the mouth together with the bread, as some of Wittenberg have taught.",
   "> We confess that the benefit of the Supper, which is the forgiveness of sins and union with Christ, comes to the receiver by faith alone; and that the unbelieving receive the sign to their judgment, and not the thing signified to their benefit.",
   "> Therefore we bid our churches not to dispute further whether Christ is present by the consecration or by the receiving, since we have said that he is present by the one and given by the other."],
  "The council of Lambeth", "The Lord's Supper", ["cranmerian"])

T("src-capitulation-wittenberg", "Articles of the Capitulation of Wittenberg", SRC, "19 May 1547", 1547,
  "The terms by which the Ernestine elector gives up the city and the electoral title.",
  ["The terms follow the rout at Mühlberg ([[muhlberg]], [[schmalkaldic-war]], [[capitulation-of-wittenberg]]).",
   "> I. John Frederick, late Elector of Saxony, yields the city of Wittenberg with its castle, its arms and its university into the hands of His Imperial Majesty.",
   "> II. He renounces the electoral dignity and the lands attached to it, which His Majesty bestows on his cousin Maurice. He keeps the lands and towns of Thuringia for himself and his heirs, as a duke.",
   "> III. He shall stay in His Majesty's keeping until the peace be made, and shall do nothing against the Emperor or the Empire.",
   "> IV. The preachers and professors of Wittenberg shall not be harmed in their persons or their goods for what they have taught, until His Majesty's religious order be published.",
   "> V. The League of Schmalkalden is dissolved, and its alliances, its common chest and its captains are given up."],
  "Imperial commissioners", "The surrender of Wittenberg", ["gnesio-catholic"])

T("src-cranmer-invitation", "Cranmer's Invitation to the Evangelical Churches", SRC, "1548", 1548,
  "A letter that invites the beaten churches of Germany and the Swiss cities to a council in England.",
  ["Sent in the year after the League was destroyed ([[schmalkaldic-war]]), to Melanchthon, Bullinger, Bucer, Vermigli and à Lasco ([[lambeth-council]]).",
   "> To our brethren in Christ, health.",
   "> You have seen what the sword has done. The princes who were your shield are taken or scattered, and the Emperor will make an order for you which you did not choose. We do not write to stir you to a war; we write to ask you to a council.",
   "> The King of England, our young master, and his counsellors will give you a roof, a hall and safe conduct. We ask nothing of you but that you come with open hands, and that you bring the confession of your churches, that we may see in what we agree and in what we may bear with one another.",
   "> We do not mean to make one church of all. We mean to make one table, at which the churches that confess Christ alone may sit without anathema.",
   "> From Lambeth, in the second year of the King."],
  "Thomas Cranmer", "The invitation to Lambeth", ["cranmerian"])

T("src-calvin-refusal", "Calvin's Reply to the Lambeth Formula", SRC, "1552", 1552,
  "A letter that declines to sign the eucharistic formula.",
  ["Calvin and the Geneva church stay outside the Communion ([[calvin]], [[hardline-reformed]], [[lambeth-formula]]).",
   "> To the most reverend Archbishop of Canterbury.",
   "> I would gladly be one with you, and I thank you for the pains you have taken. But I cannot subscribe to a presence that does not wait for faith. You say that Christ is present by the consecration, whether the receiver believes or not. I say that he is given where he is received, and that to set his presence in the prayer of a minister is to give the minister what belongs to the Spirit.",
   "> I know that your meaning is not Rome's. But the simple will not know it, and the ministers who come after you will make of it what they please.",
   "> We shall not write against you, and we shall not be your enemies. We beg you only not to ask of us what we cannot do."],
  "John Calvin", "Geneva's refusal", ["hardline-reformed"])

T("src-settlement-1577", "Articles of the Settlement of France", SRC, "1577", 1577,
  "The framework that gives France its Gallican–Augustinian settlement and protects the Cranmerian Huguenots.",
  ["The edict's name and date are not fixed in canon ([[poissy]], [[edict-for-huguenots]]). This draft follows the proposed ratification of 1576–77.",
   "> I. The Primate of Lyon shall convene the national synod of the Church of France, and shall hear the appeals of its bishops.",
   "> II. The King shall name the bishops, as the Concordat provides, and the Pope shall confirm them. The decrees of the council of Trent shall not be published in the Kingdom.",
   "> III. Those of the Reformed religion who hold the confession of Lambeth shall be suffered to live in their towns and to worship in the places the edict names, and shall not be troubled in their goods or their persons.",
   "> IV. Those who have followed Geneva and not Lambeth shall be suffered in their present places, and in no other.",
   "> V. The Admiral and the Princes of the blood shall be the guarantors of this peace."],
  "The Crown, in the name of the King", "The settlement of the French wars", ["gallican-church", "cranmerian"],
  open_q=["The real name and date of the edict."])

T("src-filaret-excerpt", "From the Catechism of Patriarch Filaret", SRC, "1627", 1627,
  "An excerpt on Christ's work, in the Russian church's catechism.",
  ["The catechism teaches penal substitution and dual imputation ([[filaret-catechism]], [[filaret]]). The Kievan critics object ([[kiev-resisters]]); Zizanius is a source ([[lavrentiy-zizanius]]).",
   "> Q. Why did Christ suffer on the cross?",
   "> A. Because our sins were laid upon him, and he bore the punishment that was ours. In him the wrath of God against sin was spent, so that we might be quit of it.",
   "> Q. How are we made righteous?",
   "> A. Our sin is reckoned to Christ, and his righteousness is reckoned to us, and so we stand before God as those who have kept the law. But this is not all: through the Spirit we are made partakers of the divine nature, and the image that was lost is restored in us.",
   "> Q. Is the book of Wisdom Scripture?",
   "> A. It is a book of the apostolic tradition, handed down from the time of the second temple, and the Church reads it for instruction, but it is not set beside the books which Christ and his apostles cited."],
  "Patriarch Filaret and his drafters", "The Russian catechism", ["russian-orthodox"])

T("src-jerusalem-decree", "Decree of the Synod of Jerusalem on the Armenian Church", SRC, "1672", 1672,
  "The synod's act of agreement with the Armenian Church.",
  ["The synod sits as the Greek world's answer to Trent and Florence ([[synod-of-jerusalem-1672]], [[dositheos-of-jerusalem]], [[hakob-iv-julfa]]).",
   "> We, the patriarchs and bishops here gathered, with the Catholicos of the Armenians and his bishops, declare that we confess one Christ, perfect God and perfect man, and that the Word of God made flesh is one incarnate nature of God the Word, as holy Cyril taught.",
   "> We, the Greeks, receive that formula as orthodox. We, the Armenians, confess that the two natures of which the council of Chalcedon spoke are not a division, and that we do not hold with Nestorius.",
   "> Each church shall keep its own liturgy, its own calendar and its own bishops. Where we are scattered among each other in the cities of the Sultan and of the Franks, our faithful may receive the mysteries from either.",
   "> We shall open schools for the instruction of the clergy, and we shall print the books of our rites from corrected texts, that those who come after us may be taught and may teach."],
  "The Synod of Jerusalem", "Agreement with the Armenians; reform of liturgy and seminaries", ["eastern-orthodox", "miaphysite"])

T("src-bossuet-catechism", "From the Catechism of the Gallican Church", SRC, "1690s", 1695,
  "The passage on councils that causes the controversy.",
  ["The passage says the canons of Constance and Basel bind because the pope confirms them ([[gallican-catechism]], [[bossuet]]).",
   "> Q. Do the councils of Constance and of Basel bind the faithful?",
   "> A. Their canons bind, for they were confirmed by the Pope. It is not the number of the bishops nor the voice of the Kings that gives a council its force; it is that the head and the members are one body, and that the head consents.",
   "> Q. Then the Pope is above a council?",
   "> A. The Pope is the head, and a head is not above the body; but the body does nothing as a body without its head. This is the doctrine of the Church of France, which has never been in opposition to the Apostolic See."],
  "Jacques-Bénigne Bossuet", "The catechism's disputed passage", ["gallican-church"])

T("src-proclamation-charles-ii", "Proclamation of Charles II by the Royalist Council", SRC, "1645", 1645,
  "The Royalists proclaim the deposed king's son.",
  ["Issued after Naseby ([[naseby]], [[english-war]], [[charles-ii]]).",
   "> Whereas our late sovereign lord has put himself into the hands of his enemies and, by the choice of the Commons, no longer governs as a king of England ought, we the bishops, peers and officers of the Navy and the kingdom do declare that his son Charles is our lawful King.",
   "> We protest that we make no change in religion, nor in the laws of the realm; we restore the old constitution and the order of bishops as it stood.",
   "> God save the King."],
  "The Royalist Council", "The proclamation of Charles II", ["cranmerian", "byzantinists"])

# ================================================================ Chronicles and newspapers
T("chr-muhlberg", "A Relation of the Battle at Mühlberg", CHR, "May 1547", 1547,
  "A Saxon chronicler's account of the day the army was lost.",
  ["The account is in a Wittenberg chronicler's voice ([[muhlberg]], [[schmalkaldic-war]]).",
   "> On the twenty-fourth of April, a Sunday, the Emperor's army came down to the Elbe before light and found a ford which our scouts had not marked. The fog was so thick that we heard the horses before we saw them.",
   "> The Elector was at his sermon when the Spanish were across. By ten of the clock there was no army to command.",
   "> Our lord was taken in the wood, wounded in the face, and brought to the Emperor. They say that the Emperor looked at him and said nothing for a long while. We do not know what the Emperor thought. We know what the people of Wittenberg thought, who counted the carts that did not come back."],
  "A Saxon chronicler", "Mühlberg", ["gnesio-catholic"])

T("chr-london-naseby", "The London Intelligencer on Naseby", CHR, "June 1645", 1645,
  "A newsbook report from the Reforming Crown's side after the defeat.",
  ["A newsbook's voice, hostile to the victors ([[naseby]], [[prince-rupert]], [[english-war]]).",
   "> From Northampton, the sixteenth of June. It is certain that Prince Rupert's horse have broken the right wing of the army, and that our foot have been cut to pieces upon the hill. The King has fled; his Majesty's coach was taken, and many papers in it.",
   "> The Royalists give out that they are for the Church and the constitution. We have noted that they have the Church of England's bishops on their side, and the Navy. It seems the Navy does not care for the King's reforms, and the bishops do not care for his conscience.",
   "> We are told that they will now proclaim the young prince. We pray that God will have mercy on the poor commons, who have trusted a King, and been left by him."],
  "A London newsbook", "Naseby", ["cranmerian"])

T("chr-magdeburg", "A True Relation of the Sack of Magdeburg", CHR, "May 1631", 1631,
  "A Gnesio-Catholic account of the burning of the city.",
  ["A relation circulated from Hamburg and Stockholm ([[sack-of-magdeburg]], [[tilly]], [[siege-magdeburg]]).",
   "> The twentieth of May, in the morning, the Imperialists came in by the gate that was not guarded. By noon the whole city was on fire, and the cathedral was full of those who had fled for sanctuary. There was no quarter.",
   "> The city that refused the Interim, and stood a siege in the year fifty and fifty-one, is now a field of ash. Flacius would have wept. We are told that the Count Tilly was not able to stop it.",
   "> Let it be known to all Christians what the Emperor's friends do."],
  "A Hamburg printer", "The sack of Magdeburg", ["gnesio-catholic"], st="prop")

T("chr-dort", "A Report from Dort", CHR, "May 1619", 1619,
  "An Amsterdam courant on the end of the synod and the execution at The Hague.",
  ["The courant's voice ([[synod-of-dort]], [[oldenbarnevelt]], [[maurice-of-nassau]], [[gomarus]]).",
   "> The synod of Dort is ended, and the doctrine of the Remonstrants is condemned in five articles. The Remonstrant ministers are deposed and some banished.",
   "> At The Hague, on the thirteenth of May, the Advocate of Holland, Mr. Johan van Oldenbarnevelt, was beheaded in the court of the Binnenhof, in the seventy-second year of his age. He walked to the scaffold with a staff, and spoke to the people.",
   "> It is observed that the Archbishop of Canterbury's divines sat at the synod, and did not all agree with the verdict."],
  "An Amsterdam courant", "Dort and the execution", ["cranmerian"])

T("chr-lyon-gazette", "The Gazette of Lyon on the Ratification", CHR, "1577", 1577,
  "A Lyon report on the settlement's ratification.",
  ["A Gallican voice ([[src-settlement-1577]], [[poissy]], [[coligny]]).",
   "> The King has set his hand to the peace. The Primate of Lyon is to sit as judge of the Church of France, and the Admiral is to be guarantor for those of the Religion. The Parlement of Paris resists, but is not heard.",
   "> It is said that the Admiral came to the city in a plain coat. He heard Vespers in the cathedral and said that he had not found the music so ill."],
  "A Lyon gazette", "The French settlement", ["gallican-church", "cranmerian"])

T("chr-constantinople-avviso", "An Avviso from Constantinople on the Synod of Jerusalem", CHR, "1672", 1672,
  "A Venetian report to the Doge on the Greek-Armenian agreement.",
  ["A Venetian newsletter ([[synod-of-jerusalem-1672]], [[hakob-iv-julfa]], [[voskan-yerevantsi]]).",
   "> The Greek patriarchs are lately come back from Jerusalem and report that they and the Armenian Catholicos have signed a concord on the nature of Christ. It is thought to be a thing of great consequence, for the Armenians are many, and spread over all the trade of the East.",
   "> The Sultan's ministers have not forbidden it. The Franks of Galata are alarmed, and the Jesuits say it is a contrivance of the Muscovites against Rome; but the Muscovites are said to be displeased.",
   "> The printing of books is to begin at Constantinople in the coming year."],
  "A Venetian informant", "The Synod of Jerusalem", ["eastern-orthodox", "miaphysite"])
