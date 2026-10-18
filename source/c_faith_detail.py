"""Beliefs, structure and principal figures for each faith. Statuses follow the faith entry itself;
where a belief is proposed rather than canon, the text says so."""

DETAIL = {}

DETAIL["roman-catholic"] = dict(
  beliefs=[
    ["Justification", "Trent's Session 6 is softened ([[council-of-trent]]): imputed righteousness may stand beside inherent righteousness. Session 5 on original sin stands as written. The Roman communion can therefore read much of the evangelical case on justification inside its own bounds."],
    ["Sacraments", "Seven sacraments, transubstantiation, the sacrifice of the Mass, the communion of saints. Communion in both kinds is a matter of discipline and is granted to the Utraquist rite ([[utraquist-rite]])."],
    ["Authority", "Scripture and tradition, interpreted by the magisterium. Papal primacy of jurisdiction, though the French settlement shows how much room it leaves in practice ([[gallican-church]])."],
    ["Grace and nature", "A more Augustinian tone than in history, helped by the Spirituali ([[spirituali]]) and by Louvain ([[baianists]]). The Molinist–Thomist quarrel over grace and free will goes on inside the Jesuit and Dominican schools."]],
  structure=["Pope and curia at Rome; cardinals in consistory; bishops nominated by local custom or by the Crown and confirmed by Rome (the Concordat of Bologna, [[concordat-of-bologna]]). Religious orders answer to their own generals. The Jesuits ([[jesuits]]) are the most active teaching order.",
             "Internal parties: the Spirituali, who prevail at Trent, and the hard-line Zelanti ([[zelanti]]) who keep their influence in the Curia."],
  theologians=["ignatius-loyola", "robert-bellarmine", "peter-canisius", "francisco-suarez", "luis-de-molina", "charles-borromeo", "teresa-of-avila", "cajetan", "gasparo-contarini", "reginald-pole", "johann-eck", "gian-pietro-carafa", "paolo-sarpi", "erasmus", "thomas-more"])

DETAIL["gallican-church"] = dict(
  beliefs=[
    ["Gallican liberties", "The Crown nominates and Rome confirms. A general council stands above the pope in disputes about the Church's constitution. The Tridentine decrees are never received in France."],
    ["Doctrine", "An Augustinian theology of grace, with its own catechism issued from Lyon. The treatment of concupiscence is a point of friction with Louvain ([[baianists]])."],
    ["Eucharist", "Transubstantiation, as in Rome. The Cranmerian Huguenots who live under the same Crown accept the Lambeth formula ([[lambeth-formula]]) instead."]],
  structure=["The Primate of Lyon ([[alphonse-de-richelieu]], [[pierre-d-epinac]]) convenes the national synod and acts as court of appeal. The Crown nominates bishops. Rome confirms them and keeps the communion. The Parlement of Paris ([[parlement-paris]]) is a watchful civil check."],
  theologians=["francis-de-sales", "du-perron", "pierre-de-berulle", "bossuet", "baius", "jansen"])

DETAIL["utraquist-rite"] = dict(
  beliefs=[
    ["Communion in both kinds", "The chalice for the laity, the old Hussite sign, now permitted by Rome as part of the settlement."],
    ["Vernacular liturgy", "Mass in Czech. Roman doctrine and papal primacy, which the Utraquists accept in return."],
    ["Justification", "Trent's softened Session 6 makes the union possible: the old Utraquist position on faith and works is no longer heretical."]],
  structure=["Under the Archbishop of Prague ([[harrach]]), in full union with Rome. It is modelled on the Union of Brest ([[brest]]) but in a Western rite."],
  theologians=["jan-rokyta"])

DETAIL["gnesio-catholic"] = dict(
  beliefs=[
    ["Justification", "By faith alone, as Luther taught, with the 1530 Augsburg Confession ([[augsburg-confession]]) as the legal banner."],
    ["Sacraments", "Seven sacraments and the real, bodily presence in the Eucharist. It rejects the Lambeth formula's spiritual presence ([[lambeth-formula]]) as too thin, and transubstantiation as too philosophical."],
    ["Church", "The first seven ecumenical councils. Ordination in the historic succession, carried through the Swedish line ([[petrus-magni]], [[laurentius-petri]])."],
    ["Adiaphora", "No ceremony may be imposed under pressure, which is the principle of the refusal of the Interim ([[augsburg-interim]], [[siege-magdeburg]])."]],
  structure=["Bishops in the historic succession, with synodal government. The union with the Bohemian Utraquists in 1575 ([[bohemian-union-1575]]) gave it its name. Three branches: the independent churches led from Uppsala ([[gnesio-independent]]), the Lyon-aligned Rhenish churches ([[gnesio-lyon]]) and the Orthodox-aligned churches ([[gnesio-orthodox]])."],
  theologians=["martin-luther", "flacius", "amsdorf", "johannes-wigand", "martin-chemnitz", "johann-gerhard", "laurentius-petri", "jonas-bretkunas"])

DETAIL["cranmerian"] = dict(
  beliefs=[
    ["The Lambeth formula", "Christ is spiritually present in the Supper through the Spirit and the consecration. The presence does not depend on the faith of the receiver, but the benefit does ([[lambeth-formula]]). This rejects transubstantiation, the Lutheran bodily presence and pure receptionism. The classical exposition is John Cosin's ([[john-cosin]])."],
    ["Justification", "By faith alone, in the evangelical sense of the Augsburg Confession ([[augsburg-confession]]) as read by Melanchthon."],
    ["Liturgy", "The Book of Common Prayer ([[book-of-common-prayer]]) in English, and vernacular liturgies on its pattern elsewhere."],
    ["The formula and the hardliners", "The formula is why the stricter Calvinists will not join: they hold that the presence is given only in the believing reception ([[hardline-reformed]])."]],
  structure=["Two systems overlap. Bishops govern by diocese. Archpresbyters govern regions as the analogue of dioceses. A bishop and an archpresbyter are counterparts, and each can stand in the other's place at councils.",
             "Presbyterian consistories and synods sit under both and often overlap with them, so the lines of authority are tangled. It works by custom rather than by design: the continental churches brought superintendents and consistories ([[johannes-bugenhagen]]) and England brought bishops. Canterbury is the senior see, but it does not rule the Communion."],
  theologians=["cranmer", "melanchthon", "bucer", "vermigli", "a-lasco", "bullinger", "hemmingsen", "brenz", "john-jewel", "richard-hooker", "john-cosin", "zacharias-ursinus", "johannes-bugenhagen", "matthew-parker"])

DETAIL["hardline-reformed"] = dict(
  beliefs=[
    ["Eucharist", "The presence is spiritual and given only to the believing receiver. The Lambeth formula's presence through consecration alone ([[lambeth-formula]]) seems to them to come too close to the Roman and Lutheran errors."],
    ["Predestination", "Double predestination in the Genevan sense, which later becomes the issue at Dort ([[synod-of-dort]])."],
    ["Worship", "Scripture alone regulates worship. Plain churches, no ceremonies without a command."]],
  structure=["Presbyterian: ministers, elders and deacons; consistory, presbytery, provincial and national assembly. No bishops. The Geneva Company of Pastors and the Scottish General Assembly are the model. Their parity with the Communion's archpresbyters is the point of contact, and the source of confusion, with the Cranmerian churches."],
  theologians=["calvin", "beza", "knox", "andrew-melville", "gomarus", "jeanne-d-albret"])

DETAIL["byzantinists"] = dict(
  beliefs=[
    ["Eucharist", "A high reading of the Lambeth formula: the presence through consecration ([[john-cosin]]), with an emphasis on epiclesis taken from the Greek liturgies."],
    ["Fathers and councils", "The Greek Fathers and the first seven councils as the standard. A hope for communion with Constantinople."],
    ["Monarchy", "An autocratic Christian emperor-king, on a Roman and Byzantine model. This is a political theology as much as a doctrinal one."]],
  structure=["An Anglican party, not a separate church, rooted in the West Country. Its bishops and clergy sit within the Communion's episcopal order, but a faction wants a stronghold in the West and direct talks with Constantinople."],
  theologians=["lancelot-andrewes", "john-cosin", "edward-pococke", "patrick-young", "thomas-roe"])

DETAIL["evangelical-unaligned"] = dict(
  beliefs=[["Justification", "Evangelical, by faith alone, but without commitment to either Wittenberg party. Prussia was caught up in Osiander's controversy ([[osiander]]) rather than in the Philippist–Gnesio split."]],
  structure=["Local church orders in Courland and Livonia under their dukes and city councils; no common hierarchy."],
  theologians=["osiander"])

DETAIL["unity-brethren"] = dict(
  beliefs=[
    ["Heritage", "The Hussite tradition of the Bohemian reformation, with a strong discipline and a practical ethic."],
    ["Eucharist", "Spiritual presence, close to the Lambeth formula ([[lambeth-formula]]), which eased their entry to the Communion."]],
  structure=["Bishops (seniors) and a synod; local congregations and strict discipline. After 1575 they join the Cranmerian communion ([[cranmerian]])."],
  theologians=["comenius", "jan-blahoslav", "jan-rokyta"])

DETAIL["unitarian"] = dict(
  beliefs=[["Antitrinitarianism", "God is one person. Christ is divine in an office or by adoption, not co-equal in essence. Preaching is protected by the Edict of Torda ([[torda]])."],
           ["Worship", "Simple, centred on preaching. No adoration of Christ in the Dávid party."]],
  structure=["A superintendent (bishop) in Kolozsvár and congregational synods, recognised by the principality's Diet as one of its legitimate religions."],
  theologians=["ferenc-david", "giorgio-biandrata"])

DETAIL["polish-brethren"] = dict(
  beliefs=[["Antitrinitarianism", "Socinian: Christ is a man raised to divinity, rationalist reading of Scripture."],
           ["Ethics", "Strong pacifism and refusal of public office in many congregations."]],
  structure=["Congregations and a synod, with Raków as the intellectual centre."],
  theologians=["faustus-socinus", "giorgio-biandrata"])

DETAIL["anabaptist"] = dict(
  beliefs=[["Believer's baptism", "Baptism is for adults who confess. The church is a gathered community."],
           ["Separation", "Many refuse oaths and arms; Hutterites hold property in common ([[jakob-hutter]])."]],
  structure=["Local congregations with elders; no state church. The Mennonites ([[menno-simons]]) in the north and Hutterite communities in Moravia."],
  theologians=["menno-simons", "balthasar-hubmaier", "thomas-muntzer", "jakob-hutter"])

DETAIL["eastern-orthodox"] = dict(
  beliefs=[
    ["Theosis and the Fathers", "The first seven councils, the Greek Fathers, the liturgy as the centre of faith."],
    ["The catechism question", "The Greek and Kievan churches reject Filaret's catechism ([[filaret-catechism]]) with its penal substitution and dual imputation. Lucaris' Calvinising confession was condemned in history, and the same question now falls on Moscow's text."]],
  structure=["Patriarchates (Constantinople, Alexandria, Antioch, Jerusalem), the Serbian Patriarchate of Peć and the self-governing Archbishopric of Ohrid. Kiev's metropolitan holds a seat in Poland-Lithuania, alongside the Uniate rival ([[ruthenian-uniate]])."],
  theologians=["dositheos-of-jerusalem", "cyril-lucaris", "peter-mohyla", "maximus-the-greek", "nil-sorsky", "joseph-volotsky"])

DETAIL["russian-orthodox"] = dict(
  beliefs=[
    ["The catechism of 1627", "Filaret's catechism ([[filaret-catechism]]): material sufficiency of Scripture, the deuterocanon as Second Temple apostolic tradition, penal substitution and dual imputation."],
    ["The Kiev resisters", "Kievan scholars object to the catechism ([[kiev-resisters]]). After Pereiaslav ([[pereiaslav]]) they are absorbed in Moscow and bring their own scholastic learning."],
    ["Ritual", "The Stoglav ([[stoglav]]) rules on ritual and discipline; the church holds that Moscow is the heir of the Greek tradition."]],
  structure=["A patriarchate since 1589 ([[job]]). The patriarch is first among bishops but works alongside the tsar. The Western-Rite church ([[western-rite-orthodox]]) is a vicariate."],
  theologians=["filaret", "lavrentiy-zizanius", "simeon-polotsky", "feofan-prokopovich", "maximus-the-greek", "nil-sorsky", "joseph-volotsky", "hermogenes"])

DETAIL["western-rite-orthodox"] = dict(
  beliefs=[["Orthodox creed", "The Nicene creed without the filioque, and leavened bread, given up as the price of recognition."],
           ["Western liturgy", "A Latin or vernacular Western liturgy retained, with a theology close to Gnesio justification ([[gnesio-orthodox]])."]],
  structure=["Primate at Narva, in 1635 Johannes Matthiae ([[johannes-matthiae]]), under the Patriarch of Moscow as a vicariate and protected by treaty inside Gnesio-Catholic Sweden."],
  theologians=["johannes-matthiae", "jan-rokyta", "andrey-kurbsky"])

DETAIL["ruthenian-uniate"] = dict(
  beliefs=[["Union with Rome", "Papal primacy accepted, the filioque tolerated in the Roman creed. The Eastern rite, married clergy and the Byzantine liturgy are kept ([[brest]])."]],
  structure=["The Uniate Metropolitan of Kiev ([[josyf-rutsky]]) and bishops, in communion with Rome. Orthodox parishes and brotherhoods stay outside."],
  theologians=["hypatius-pociej", "josyf-rutsky", "josaphat-kuntsevych"])

DETAIL["sunni"] = dict(
  beliefs=[["Law", "Hanafi in the Ottoman lands, Maliki in North Africa. Suleiman's qanun and the sharia are joined under the Şeyhülislam ([[ebussuud]])."],
           ["Revival", "Reformers such as Birgivi ([[birgivi]]) demand strict adherence."]],
  structure=["The Ottoman sultan holds the caliphal claim from 1517 ([[ridaniya]]). Ulema, muftis and the Şeyhülislam. Morocco has its own sultanate."],
  theologians=["ebussuud", "birgivi"])

DETAIL["shia"] = dict(
  beliefs=[["Twelver doctrine", "Twelve imams, the hidden imam, state-sponsored mourning rites."],
           ["Philosophy", "The Isfahan school: Mulla Sadra's transcendent theosophy ([[mulla-sadra]]) and Baha al-Din al-Amili ([[shaykh-bahai]])."]],
  structure=["Safavid shahs and Persian ulema, with Arab Jabal Amil scholars invited by Tahmasp ([[al-karaki]]). Zaydi imams govern the Yemen highlands ([[al-mansur-al-qasim]])."],
  theologians=["al-karaki", "shaykh-bahai", "mulla-sadra", "al-mansur-al-qasim"])

DETAIL["ibadi"] = dict(
  beliefs=[["Imamate", "An elected imam, a distinct and moderate Ibadi theology."]],
  structure=["Oman's imamate, with a tribal consultative council."],
  theologians=["nasir-bin-murshid"])

DETAIL["judaism"] = dict(
  beliefs=[["Halakha", "Karo's Shulchan Aruch with Isserles' glosses ([[joseph-karo]], [[moses-isserles]]) become the common code."],
           ["Kabbalah", "Safed's mystics, Luria in particular ([[isaac-luria]])."]],
  structure=["Local kehillot and rabbinic courts. The Council of Four Lands governs Polish and Lithuanian Jews from the 1580s. Joseph Nasi ([[joseph-nasi]]) is a patron in the Ottoman world."],
  theologians=["joseph-karo", "moses-isserles", "isaac-luria", "maharal", "joseph-nasi"])

DETAIL["miaphysite"] = dict(
  beliefs=[["Christology", "One incarnate nature of the divine Word, the Cyrilline formula. The Armenian Church accepts at Jerusalem in 1672 that Chalcedon's two natures are not Nestorian, and the Greeks accept the formula as orthodox ([[synod-of-jerusalem-1672]]). The Copts and Syriacs keep the older position."]],
  structure=["Separate patriarchates: Alexandria, Etchmiadzin, Sis, Mardin, and the Ethiopian metropolitan. Emperor Susenyos' conversion to Rome in 1622 splits Ethiopia ([[susenyos]])."],
  theologians=["hakob-iv-julfa", "voskan-yerevantsi"])

DETAIL["church-east"] = dict(
  beliefs=[["Christology", "The East Syriac tradition, outside the Chalcedonian and the Miaphysite camps."]],
  structure=["A patriarch at Rabban Hormizd, with metropolitans in northern Iraq."],
  theologians=[])

DETAIL["maronite"] = dict(
  beliefs=[["Roman communion", "In communion with Rome, with a Syriac liturgy."]],
  structure=["A patriarch in Mount Lebanon, under Ottoman rule."],
  theologians=[])

DETAIL["traditional-religions"] = dict(
  beliefs=[["Diverse practice", "Ancestral religion, shamanism and local cults, mapped as one category."]],
  structure=["Local authorities: lineage elders, chiefs, shamans. Missionary Christian and Muslim communities appear as dots on the map."],
  theologians=[])
