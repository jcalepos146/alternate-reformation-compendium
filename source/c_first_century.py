"""Author-approved first-century revisions, applied after the earlier decisions.

Military settlements and church constitutions are alternate-history canon.
Unsettled details remain explicit questions rather than invented quotations.
"""
from common import ENT, E, M, RH
from c_decisions import D, fact

by = {e['id']: e for e in ENT}


def doc(id, name, when, y, summary, body, parties, effect, faith):
    E(id, 'doc', name, 'canon', when, y, summary, body,
      facts=[['Date', when], ['Kind', 'Settlement'], ['Parties', parties], ['Effect', effect]],
      faith=faith)


D('marignano', body=[
    'On 13–14 September 1515 Francis I and his Venetian allies defeat the Swiss near Milan during the War of the League of Cambrai. Huldrych Zwingli accompanies the Glarus contingent as chaplain. Historically he survived; in this timeline he is killed. His death is the point of divergence, before his ministry at Einsiedeln or his appointment in Zurich.',
    'The Swiss defeat still damages the prestige of mercenary warfare, but there is no returning Zwingli to turn his experience into a reforming ministry. Zurich remains Roman in 1525. Luther’s challenge in Wittenberg develops independently; Swiss reform later proceeds through [[leo-jud]], [[bullinger]] and the exchanges with Basel and Strasbourg.',
    'The historical Zurich circle of Zwingli’s students does not form in the same way. This removes that particular origin of Swiss Anabaptism, rather than every independent radical movement. The historical Kappel Wars do not occur; the later [[zurich-settlement]] establishes a different accommodation between the cantons.'
])

doc('zurich-settlement', 'The Zurich Crisis and Cantonal Settlement', 'Late 1520s–early 1530s', 1530,
    'A brief internal crisis produces a delayed Zurich Reformation and a negotiated peace with the Catholic cantons.', [
    'Without Zwingli’s preaching campaign, evangelical reform reaches Zurich through visiting preachers, print and correspondence with Basel and Strasbourg. [[leo-jud]] becomes its leading local minister. Reform divides the council, guilds and clergy before a brief internal crisis forces a settlement.',
    'The council authorizes reform within Zurich while negotiating coexistence with the Catholic cantons. Neither side secures a right to impose its confession on the other. The settlement avoids the historical Kappel campaigns without assuming that confessional antagonism disappears.',
    'Jud’s church grows through municipal consent and inter-cantonal compromise. [[bullinger]] inherits this settlement after Jud’s death in 1542. His later support for [[lambeth-council]] grows from an established habit of negotiating unity without requiring identical local institutions.'
    ], 'Zurich council, evangelical clergy and Catholic cantons', 'Delayed reform; negotiated cantonal coexistence', ['cranmerian', 'roman-catholic'])
D('leo-jud', body=[
    'After Zwingli’s death at [[marignano]], Jud leads Zurich’s delayed Reformation. A brief internal crisis ends in the [[zurich-settlement]], which establishes municipal reform while accommodating the Catholic cantons. He works within the Swiss and Upper German networks of preaching and correspondence rather than inheriting Zwingli’s historical movement.',
    'His moderate church gives [[bullinger]] an institutional foundation after his death in 1542. Its later openness to Lambeth develops from this negotiated beginning.'
])
D('bullinger', body=[
    'Bullinger succeeds [[leo-jud]] in a Zurich reformed through the [[zurich-settlement]]. With no Zwingli-led Reformation or historical Kappel catastrophe, his authority rests on the council settlement and on links with Basel, Strasbourg and the German evangelicals.',
    'His envoys participate in [[lambeth-council]]. Zurich’s acceptance links Swiss reform to the wider Communion, while the Second Helvetic Confession later supplies a route for the Hungarian Reformed. His moderation does not erase disputes about consecration, ministry or synodal government.'
])

D('schmalkaldic-war', when='1546–49', y2=1549,
  sum='A prolonged war ending in a negotiated imperial victory and dissolution of the League.',
  body=[
    'The Danube campaign of 1546 exposes the League’s poor coordination. Charles V wins at [[muhlberg]] in April 1547, captures John Frederick and transfers the Saxon electorate to [[maurice-of-saxony]] through the [[capitulation-of-wittenberg]]. This defeats the principal Saxon army but does not end resistance throughout Germany.',
    'Surviving contingents, fortified towns and disputes over the enforcement of the [[augsburg-interim]] prolong the conflict through 1548. Imperial troops can win battles more readily than they can finance permanent occupation. The remaining resistance cannot restore the League’s strategic position, but it can make unconditional submission costly.',
    'A negotiated settlement in 1549 dissolves the League and accepts the Emperor’s political victory. Surviving princely houses retain their dynasties under restrictions on armed association; the religious settlement remains disputed. The victory is decisive in constitutional and military terms without requiring the destruction of every evangelical army or town.',
    'This insecure peace drives the churches toward [[lambeth-council]]. England offers a meeting place beyond imperial jurisdiction. Trent’s softened Session 6 of January 1547 ([[council-of-trent]]) precedes Mühlberg: it belongs to the search for religious accommodation during the war and cannot be an effect of a victory not yet won.'
  ], open_q=[])
fact('schmalkaldic-war', 'Date', '1546–49')
fact('schmalkaldic-war', 'Result', 'Negotiated imperial victory; League dissolved in 1549')
D('muhlberg', sum='Imperial victory that destroys the principal Saxon army, but does not end the wider war.',
  body=[
    'On 24 April 1547 the imperial army crosses the Elbe, defeats the Saxon field army and captures John Frederick. The [[capitulation-of-wittenberg]] follows in May, transferring the electorate to Maurice.',
    'The defeat breaks the League’s strongest Saxon position. Other contingents and fortified towns continue resistance, extending the [[schmalkaldic-war]] until a negotiated imperial victory in 1549.'
  ])
D('capitulation-of-wittenberg', body=[
    'John Frederick yields Wittenberg and the electoral dignity to the Emperor, who grants the electorate to [[maurice-of-saxony]]. The Ernestine dynasty retains its Thuringian lands.',
    'The capitulation ends this phase of Saxon resistance. It does not end the [[schmalkaldic-war]], which continues elsewhere until the negotiated settlement of 1549.'
])
D('schmalkaldic-league', 'canon', when='1531–49', y2=1549,
  sum='The evangelical defensive league dissolved after a prolonged war and negotiated imperial victory.',
  body=['The League loses its main Saxon army at [[muhlberg]], but resistance continues elsewhere. The settlement ending the [[schmalkaldic-war]] in 1549 dissolves the alliance while preserving surviving princely houses under political restrictions. The churches seek a more durable association at [[lambeth-council]].'])

doc('piedmont-bargain', 'The Franco-Imperial Bargain over Piedmont', '1552', 1552,
    'Charles V accepts a French foothold around Turin in exchange for French neutrality during the Princes’ Revolt.', [
    'Henry II possesses bargaining power in the French occupation of Piedmont. Charles V chooses to concede ground in Italy rather than fight France and the German princes simultaneously. He accepts continued French possession of Turin and a Piedmontese foothold in exchange for French neutrality in the [[princes-revolt]].',
    'The bargain deprives Maurice’s coalition of the active French military support on which its strategy depends. It is a diplomatic exchange of territories and strategic freedom, not French approval of imperial religious policy. France can later protect evangelical clients without having rescued this revolt.',
    'Milan and Naples remain Habsburg possessions. The durable limits of the French foothold are confirmed in the revised [[cateau-cambresis]] settlement; the rights of the House of Savoy outside that foothold remain a matter for negotiation.'
    ], 'Charles V and Henry II', 'French foothold at Turin; French neutrality in Germany', ['roman-catholic', 'gallican-church'])

E('princes-revolt', 'battle', 'The Princes’ Revolt', 'canon', '1552', 1552,
  'Maurice’s pan-Protestant rising fails after France trades German intervention for a foothold in Piedmont.', [
    'Maurice turns against the imperial order he helped establish. Restrictions left by the [[schmalkaldic-war]], resentment of the Interim and fear of permanent imperial domination draw princes and churches into a pan-Protestant movement. Its political breadth exceeds the doctrinal agreement actually achieved at [[lambeth-council]].',
    'The [[piedmont-bargain]] removes active French intervention. Charles concentrates against the coalition, whose isolated forces fail to obtain the decisive strategic breakthrough. Maurice dies during the revolt; the coalition fails to force the historical settlement of Passau.',
    'Gnesio-Lutheran dissidents interpret Maurice’s death as divine judgment on religious compromise. This is their polemical claim, not the narrator’s explanation. His brother and successor [[augustus-of-saxony]] is persuaded by their cause. The defeat strengthens Gnesio influence in electoral Saxony while leaving other evangelical survivors more dependent on English and French protection.',
    'Foreign protection remains conditional: the same France that abandoned the revolt for Italian gains may later shelter its survivors. Neither foreign patron can be treated as a dependable substitute for a German military coalition.'
  ], facts=[['Date', '1552'], ['Place', 'Holy Roman Empire'], ['Sides', 'Charles V against Maurice and the allied princes'], ['Result', 'Imperial victory; Maurice killed']],
  faith=['cranmerian', 'gnesio-catholic', 'roman-catholic'])
D('maurice-of-saxony', 'canon', when='Elector 1547–52', y2=1552,
  sum='Imperial ally turned pan-Protestant leader, killed in the failed Princes’ Revolt.',
  body=[
    'Maurice gains the electoral title after [[muhlberg]] and the [[capitulation-of-wittenberg]]. He helps enforce the imperial order, including the [[siege-magdeburg]], before turning against the restrictions and religious pressure that accompany it.',
    'He leads the pan-Protestant [[princes-revolt]] of 1552. France’s neutrality under the [[piedmont-bargain]] helps doom the coalition. He dies during the revolt, rather than at Sievershausen in 1553 as historically. Gnesio dissidents proclaim his death divine judgment, and his successor [[augustus-of-saxony]] accepts their religious cause.'
  ], basis=RH, open_q=[])
M('augustus-of-saxony', 'Augustus, Elector of Saxony', 'canon', 'Elector 1552–86', 1552,
  'Maurice’s brother and successor, persuaded by the Gnesio interpretation of the failed revolt.', [
    'Augustus succeeds when [[maurice-of-saxony]] dies in the [[princes-revolt]] of 1552. Gnesio-Lutheran dissidents interpret the defeat as judgment on Maurice’s compromises, and Augustus becomes convinced of their cause.',
    'His accession disrupts the earlier Philippist ascendancy in Albertine Saxony. Philippist ministers and scholars remain, but they no longer enjoy an assured monopoly of princely support. This changes the balance within Germany without turning the Gnesio party into an ally of Lambeth.',
    'The existing later-century and seventeenth-century entries assume a Cranmerian Saxon court. How that later alignment emerges after this Gnesio turn remains unsettled; it must not be projected backward onto Augustus’s accession.'
  ], ['gnesio-catholic'], 'Elector of Saxony', 'Augustus, Elector of Saxony', basis=RH, y2=1586,
  open_q=['How the Gnesio turn under Augustus gives way to the later Cranmerian court already recorded in the compendium.'])
D('peace-of-passau', 'canon', name='The Failed Passau Settlement',
  sum='The unsuccessful attempt to secure the concessions granted at Passau in real history.',
  body=[
    'In real history the Princes’ Revolt obtained the Peace of Passau in 1552. Here the [[princes-revolt]] fails and Maurice dies. No equivalent successful peace is concluded on the historical terms.',
    'The surviving princes must seek concessions through later negotiation, including the [[peace-of-augsburg]], while evangelical churches rely more heavily on England and France. The later recognition of the Augsburg Confession is a concession made within an imperial victory, rather than the direct product of a successful revolt.'
  ], open_q=[])
fact('peace-of-passau', 'Effect', 'Historical concessions not secured; revolt defeated')
D('augsburg-interim', when='1548–55', y2=1555,
  body=by['augsburg-interim']['body'] + [
    'The failed [[princes-revolt]] does not secure the historical termination of the Interim at Passau. Enforcement remains uneven and contested until the [[peace-of-augsburg]] supplies a new legal framework in 1555. In Saxony, Augustus’s Gnesio turn changes the court’s response to the earlier Leipzig compromise.'
  ])
fact('augsburg-interim', 'Date', '1548–55')
D('peace-of-augsburg', body=[
    'After the failed [[princes-revolt]], the Emperor’s side negotiates from strength. Political victory nevertheless leaves the cost of enforcement and the unresolved confessional loyalties of the estates. The peace recognizes the Augsburg Confession without deciding which reading of it is protected.',
    'Both Philippists and Gnesio adherents claim its protection. The failed Passau settlement gives neither party a simple claim that armed resistance secured its liberties. The ambiguity sends disputes to the courts and Diets; Maximilian II’s tolerance later helps keep the arrangement workable.'
  ], open_q=['The precise restrictions on military association carried from the 1549 settlement into the peace of 1555.'])

D('cateau-cambresis', 'canon', sum='The Italian settlement preserves a French foothold at Turin alongside Habsburg Milan and Naples.',
  body=[
    'The peace of 1559 confirms the central exchange made in the [[piedmont-bargain]]: France retains Turin and a durable Piedmontese foothold, while Spain retains Milan and Naples. France relinquishes wider ambitions against those Habsburg possessions without surrendering its entire Italian position.',
    'The later fighting and Spanish victories at [[saint-quentin]] and [[gravelines]] bring the crowns back to negotiation. They do not undo the whole bargain by which Charles obtained freedom to defeat the [[princes-revolt]]. The result is Spanish predominance with a persistent French bridgehead, rather than an uncontested Spanish settlement of Italy.',
    'French gains demonstrate the Crown’s ability to exchange military intervention for diplomatic concessions. They strengthen its independence in European affairs, but do not themselves determine the doctrine of the Gallican Church.'
  ], open_q=['The exact boundary of the French Piedmontese foothold and the compensation and restoration granted to the House of Savoy.'])
fact('cateau-cambresis', 'Effect', 'French Turin and Piedmontese foothold; Spanish Milan and Naples')
D('metz-1552', 'canon', name='Metz and the Neutrality Bargain',
  sum='French neutrality removes the historical siege of Metz from the campaign of 1552–53.',
  body=['The historical French intervention and Charles V’s unsuccessful siege of Metz do not occur in the same form. The [[piedmont-bargain]] redirects the Franco-imperial negotiation toward Turin and allows Charles to concentrate on the [[princes-revolt]]. No French acquisition of the Three Bishoprics is assumed in this revised sequence.'])
fact('metz-1552', 'Sides', 'France and the Empire in negotiation')
fact('metz-1552', 'Result', 'Historical siege displaced by the neutrality bargain')
D('henry-ii-france', 'canon', body=[
    'Henry negotiates the [[piedmont-bargain]] with Charles V in 1552, exchanging neutrality during the [[princes-revolt]] for a durable foothold around Turin. French policy sacrifices an immediate German alliance for an Italian advantage.',
    'War with the Habsburg crowns later resumes. Spanish victories at [[saint-quentin]] and [[gravelines]] lead to the revised [[cateau-cambresis]] in 1559, which confirms French Turin alongside Spanish Milan and Naples. Henry dies in a joust that year.'
  ])
D('charles-v', 'canon', body=[
    'Charles wins at [[muhlberg]] in 1547 but must continue the [[schmalkaldic-war]] until a negotiated imperial victory in 1549. The League dissolves; surviving dynasties remain and religious enforcement proves difficult.',
    'In 1552 he accepts the [[piedmont-bargain]], conceding a French foothold around Turin to obtain neutrality in Germany. He defeats the [[princes-revolt]], in which Maurice dies. The cost of victory is a less complete Habsburg predominance in Italy and a German religious settlement that still requires negotiation at [[peace-of-augsburg]].'
  ])

doc('lambeth-constitution', 'The Apostolic Constitution of Lambeth', '1549–52', 1552,
    'A synodal episcopate and recognition of existing ministers give the Communion a shared institutional form.', [
    'Lambeth describes episcopacy as a providential yet ultimately prudential development of apostolic church order. Its constitution can therefore affirm episcopal continuity without requiring every participating church to teach that a distinct episcopal office is universally indispensable by divine command.',
    'Continental churches with Presbyterian government retain their synods and recognize their existing ministers. New bishops, chosen to represent the individual synods, receive joint ordination from an English bishop and a Lutheran superintendent. Recognition of existing ministry is not conditional on repeating the ordinations of every pastor.',
    'The synodal representatives function as bishops within the Communion. Local titles such as superintendent and archpresbyter continue, creating overlapping habits of government. Canterbury has seniority without becoming a universal court ruling all member churches.',
    'The claim to be Apostolic, Reformed Catholics rests on continuity of teaching, inherited ordination and common church order. Its critics dispute both the prudential account of episcopacy and the decision to preserve the [[unchanged-ordinal]].'
    ], 'English bishops and participating evangelical churches', 'Existing ministers recognized; new bishops jointly ordained', ['cranmerian'])
doc('unchanged-ordinal', 'The Unchanged Ordinal Controversy', '1549–52 and after', 1552,
    'Cranmer retains the inherited ordination rite for polemical purposes despite rejecting the Roman theology of the Mass.', [
    'Cranmer does not introduce the changes to the ordination rite associated with the historical Edwardian Ordinals. He preserves the inherited rite while rejecting the Roman understanding of the Mass. This decision is deliberate propaganda against Roman opponents: the reformed churches claim that they have not abandoned the historic ministry.',
    'The retained rite operates alongside the [[lambeth-constitution]], including joint ordination of new synodal bishops and recognition of existing ministers. Preservation of the rite is not an acceptance of Roman eucharistic doctrine, and it does not by itself obtain Roman recognition of the Communion’s orders.',
    'The combination is extremely controversial. Reformed opponents dispute the rites and episcopal settlement as well as the [[lambeth-formula]]. Some German principalities and Dutch towns refuse the union, though they are a minority. Scottish and French Reformed resistance makes ministry and church government central to the limits of the pan-Protestant project.'
    ], 'Cranmer, Lambeth delegates and opponents of the settlement', 'Inherited rite retained; controversy over ministry and doctrine', ['cranmerian', 'hardline-reformed', 'roman-catholic'])
D('lambeth-council', sum='The international council that answers imperial victory with a confession and an apostolic constitution.',
  body=[
    'The prolonged [[schmalkaldic-war]] ends in negotiated imperial victory in 1549. Cranmer gathers English bishops and continental representatives at Lambeth from 1549 to 1552. Melanchthon, Bullinger’s envoys, Vermigli, à Lasco and Bucer participate; Bucer dies in 1551 before the council ends.',
    'The council adopts the eucharistic [[lambeth-formula]] and the [[lambeth-constitution]]. Existing ministers are recognized. New bishops representing continental synods receive joint English–Lutheran ordination. The [[unchanged-ordinal]] supplies a controversial argument for continuity of ministry.',
    'The defeat of the [[princes-revolt]] in 1552 reinforces the need for foreign protection while exposing the limits of pan-Protestant solidarity. Gnesio dissidents reject the sacramental compromise; Reformed dissenters object to consecration, the retained rite and episcopal government. Some German principalities and Dutch towns remain outside.',
    'Mary’s restoration in England then tests whether the Communion can survive without its founding host. Continental churches shelter exiles and sustain its agreements until Elizabeth restores it in England.'
  ], open_q=['Which English bishop and Lutheran superintendent perform the first joint ordinations.'])
D('cranmer', body=by['cranmer']['body'] + [
    'His settlement includes the [[lambeth-constitution]] and the [[unchanged-ordinal]]. He rejects the Roman theology of the Mass but retains the inherited ordination rite for propaganda against Roman opponents. He also moderates royal supremacy toward a humanist account of Christian government, drawing on late Roman conceptions of Church and emperor and the political tradition exemplified by Dante’s De Monarchia. This is a development within royal supremacy, not a restoration of papal jurisdiction.'
])
D('book-of-common-prayer', 'canon', body=[
    'Cranmer’s English prayer books retain the historical publication dates of 1549 and 1552, but their eucharistic settlement must be read through the alternate [[lambeth-formula]]. Their precise wording is not assumed to be identical to the historical editions.',
    'Changes to the prayer book do not imply the introduction of the historical Edwardian Ordinals. The inherited ordination rite is retained separately under the [[unchanged-ordinal]].'
])
D('philippists', sum='Melanchthon’s followers, dominant in the wider Communion but challenged in Saxony after 1552.',
  body=[
    'The Interim divides the evangelical churches. Philippist communities in Albertine Saxony and Brandenburg enter the Lambeth network, alongside supporters elsewhere in Germany and Denmark-Norway. Their wider success gives the Cranmerian–Philippist Communion its name.',
    'Maurice’s death in the failed [[princes-revolt]] reverses their political prospects in electoral Saxony. [[augustus-of-saxony]] accepts the Gnesio cause. Philippist communities and scholars survive, but the earlier assumption of an uninterrupted Philippist electorate no longer holds.'
  ])
D('gnesio-lutherans', body=by['gnesio-lutherans']['body'] + [
    'The failed [[princes-revolt]] gives the party a new opportunity. Its dissidents interpret Maurice’s death as divine judgment, and his successor [[augustus-of-saxony]] accepts their cause. Their opposition to Lambeth can therefore coexist with participation by other evangelicals in a pan-Protestant political movement.'
])
D('cranmerian', sum='The wide evangelical communion formed at Lambeth, with a common confession and synodal episcopate.')
by['cranmerian']['body'][0] = 'Cranmer’s international council sits at Lambeth from 1549 to 1552. Philippist communities in Saxony and Brandenburg join the wider communion, but the Gnesio turn of [[augustus-of-saxony]] after 1552 prevents a simple identification of electoral Saxony with the Philippist cause. Denmark-Norway and the Hungarian Reformed later give it further strength.'
by['cranmerian']['body'].append('The [[lambeth-constitution]] recognizes existing ministers and provides joint ordination for new bishops representing synods. The [[unchanged-ordinal]] is retained despite Cranmer’s rejection of the Roman theology of the Mass. These institutional decisions are as controversial as the eucharistic agreement.')
by['cranmerian']['open_q'].append('How Saxony passes from Augustus’s Gnesio turn to its later recorded Cranmerian alignment.')
by['hardline-reformed']['body'].append('Refusal of the union also concerns the [[lambeth-constitution]] and the [[unchanged-ordinal]]. The dissenters are not a single political bloc: Scottish and French Reformed resistance coexists with minority refusals by German principalities and Dutch towns.')


