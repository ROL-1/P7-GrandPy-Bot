"""Tests file for grandPyApp/main.py."""

from grandPyApp.main import Main


class TestMain:
    """Test for class : Main."""

    def test_Main(self):
        """Main.py test."""
        question_send = "mairie caen"
        parsed_string = "mairie caen"
        geo_coord_results = [-0.333467, 49.203577]
        geo_adress_results = "11 Place François Mitterrand"
        wiki_results = "Caen (prononciation : /ˈkɑ̃/) ..."
        M = Main(question_send)
        assert M.parsed_string == parsed_string
        assert M.geo_coord_results == geo_coord_results
        assert M.geo_adress_results == geo_adress_results
        assert M.wiki_results == wiki_results
