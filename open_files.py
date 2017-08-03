def open_Kunde():
        with open("/var/www/data/Arlberghaus_Strom.xml") as a:
                Kunde_Strom = a.read()

        with open("/var/www/data/Arlberghaus_Strom_poll.xml") as b:
                Kunde_Strom_poll = b.read()

        with open("/var/www/data/Arlberghaus_Wasser.xml") as c:
                Kunde_Wasser = c.read()

        with open("/var/www/data/Arlberghaus_Wasser_poll.xml") as d:
                Kunde_Wasser_poll = d.read()

	return (Kunde_Strom, Kunde_Wasser, Kunde_Strom_poll, Kunde_Wasser_poll)
