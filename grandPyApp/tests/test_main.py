"""Tests file for grandPyApp/main.py."""

from grandPyApp.main import Main


class TestMain:
    """Test for class : Main."""

    def test_Main(self):
        """Main.py test."""
        question_send = "mairie paris"
        parsed_string = "mairie paris"
        geo_coord_results = [2.402692, 48.88214]
        geo_adress_results = (
            "Mairie, 84 Rue André Joineau, Le Pré-Saint-Gervais, Paris 93310, France"
        )
        wiki_results = "Le regard du Bernage est un regard, situé à Paris, en France."
        M = Main(question_send)
        assert M.parsed_string == parsed_string
        assert M.geo_coord_results == geo_coord_results
        assert M.geo_adress_results == geo_adress_results
        assert M.wiki_results == wiki_results
        assert isinstance(M.bonus_message, str)
        assert M.geo_fail is False
        assert M.wiki_fail is False
