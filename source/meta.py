"""English Wikipedia titles and roles for entries written before the schema had them.
The portrait app resolves each title (redirects are followed). A wrong title is reported, not guessed at."""

WIKI = {
    # popes, cardinals, bishops
    "julius-ii": "Pope Julius II", "leo-x": "Pope Leo X", "paul-iii": "Pope Paul III", "urban-viii": "Pope Urban VIII",
    "reginald-pole": "Reginald Pole", "giovanni-morone": "Giovanni Morone", "gasparo-contarini": "Gasparo Contarini",
    "cajetan": "Thomas Cajetan", "pierre-d-epinac": "Pierre d'Épinac",
    "alphonse-de-richelieu": "Alphonse-Louis du Plessis de Richelieu", "tournon": "François de Tournon",
    "cardinal-of-lorraine": "Charles, Cardinal of Lorraine", "baius": "Michael Baius", "jansen": "Cornelius Jansen",
    "harrach": "Ernst Adalbert von Harrach",
    # Wittenberg, Gnesio
    "flacius": "Matthias Flacius", "amsdorf": "Nikolaus von Amsdorf", "osiander": "Andreas Osiander",
    "abraham-angermannus": "Abraham Angermannus", "john-frederick-i": "John Frederick I, Elector of Saxony",
    "john-william-saxe-weimar": "John William, Duke of Saxe-Weimar", "john-iii-sweden": "John III of Sweden",
    "albert-of-prussia": "Albert, Duke of Prussia", "wolfgang-wilhelm": "Wolfgang Wilhelm, Count Palatine of Neuburg",
    # Cranmerian
    "cranmer": "Thomas Cranmer", "melanchthon": "Philip Melanchthon", "bucer": "Martin Bucer", "a-lasco": "Jan Łaski",
    "vermigli": "Peter Martyr Vermigli", "hemmingsen": "Niels Hemmingsen", "bullinger": "Heinrich Bullinger",
    "leo-jud": "Leo Jud", "brenz": "Johannes Brenz", "frederick-v": "Frederick V, Elector Palatine",
    "laud": "William Laud", "george-abbot": "George Abbot (archbishop of Canterbury)", "comenius": "Jan Amos Comenius",
    # hardline Reformed
    "calvin": "John Calvin", "beza": "Theodore Beza", "knox": "John Knox", "andrew-melville": "Andrew Melville",
    "jeanne-d-albret": "Jeanne d'Albret",
    # Bohemia
    "budovec": "Wenceslas Budovec", "thurn": "Heinrich Matthias von Thurn",
    # Orthodox and Eastern
    "ivan-iv": "Ivan the Terrible", "job": "Patriarch Job of Moscow", "godunov-boris": "Boris Godunov",
    "filaret": "Patriarch Filaret of Moscow", "joasaph-i": "Joasaph I of Moscow",
    "jeremias-ii": "Jeremias II of Constantinople", "cyril-lucaris": "Cyril Lucaris", "peter-mohyla": "Peter Mogila",
    "hypatius-pociej": "Hypatius Pociej", "josyf-rutsky": "Josyf Rutsky", "gedeon-balaban": "Gedeon Balaban",
    "ostrozky": "Konstanty Wasyl Ostrogski",
    # radicals
    "menno-simons": "Menno Simons", "ferenc-david": "Ferenc Dávid", "faustus-socinus": "Faustus Socinus",
    # Islam, Judaism, Ethiopia
    "ebussuud": "Ebussuud Efendi", "shaykh-bahai": "Baha al-Din al-Amili", "joseph-karo": "Joseph Karo",
    "maharal": "Judah Loew ben Bezalel", "susenyos": "Susenyos I",
    # monarchs
    "charles-v": "Charles V, Holy Roman Emperor", "ferdinand-i": "Ferdinand I, Holy Roman Emperor",
    "maximilian-ii": "Maximilian II, Holy Roman Emperor", "rudolf-ii": "Rudolf II, Holy Roman Emperor",
    "ferdinand-ii": "Ferdinand II, Holy Roman Emperor", "philip-ii": "Philip II of Spain", "philip-iv": "Philip IV of Spain",
    "francis-i": "Francis I of France", "charles-ix": "Charles IX of France", "henry-iv": "Henry IV of France",
    "louis-xiii": "Louis XIII", "gustavus-adolphus": "Gustavus Adolphus", "charles-ix-sweden": "Charles IX of Sweden",
    "sigismund-iii": "Sigismund III Vasa", "wladyslaw-iv": "Władysław IV Vasa", "christian-iv": "Christian IV of Denmark",
    "henry-viii": "Henry VIII", "edward-vi": "Edward VI", "elizabeth-i": "Elizabeth I", "james-vi-i": "James VI and I",
    "charles-i-england": "Charles I of England", "william-iii": "William III of England",
    "maurice-of-saxony": "Maurice, Elector of Saxony", "john-george-i": "John George I, Elector of Saxony",
    "george-william-brandenburg": "George William, Elector of Brandenburg", "maximilian-i-bavaria": "Maximilian I, Elector of Bavaria",
    "michael-romanov": "Michael of Russia", "suleiman": "Suleiman the Magnificent", "murad-iv": "Murad IV",
    "abbas-i": "Abbas I of Persia", "ahmad-al-mansur": "Ahmad al-Mansur", "john-sigismund": "John Sigismund Zápolya",
    "gabriel-bethlen": "Gabriel Bethlen", "george-rakoczi-i": "George I Rákóczi",
}

ROLE = {
    # existing persons that are theologians, a general or a statesman (everything else is a leader)
    "gasparo-contarini": "theologian", "cajetan": "theologian", "baius": "theologian", "jansen": "theologian",
    "flacius": "theologian", "amsdorf": "theologian", "osiander": "theologian", "melanchthon": "theologian",
    "bucer": "theologian", "a-lasco": "theologian", "vermigli": "theologian", "hemmingsen": "theologian",
    "bullinger": "theologian", "brenz": "theologian", "calvin": "theologian", "beza": "theologian",
    "andrew-melville": "theologian", "faustus-socinus": "theologian", "shaykh-bahai": "theologian",
    "joseph-karo": "theologian", "maharal": "theologian", "ferenc-david": "leader",
    "thurn": "general", "budovec": "statesman", "tournon": "leader", "cardinal-of-lorraine": "statesman",
    "knox": "leader", "comenius": "theologian",
}
