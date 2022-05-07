import pytest
from flexmock import flexmock
from mock import patch, PropertyMock
from sportsipy.ncaab.player import (AbstractPlayer,
                                    _cleanup as _cleanup_player)
from sportsipy.ncaab.roster import _cleanup, Player, Roster
from sportsipy.ncaab.teams import Teams


def mock_pyquery(url):
    class MockPQ:
        def __init__(self, html_contents):
            self.url = url
            self.reason = 'Bad URL'  # Used when throwing HTTPErrors
            self.headers = {}  # Used when throwing HTTPErrors
            self.status_code = 404
            self.html_contents = html_contents
            self.text = html_contents

    return MockPQ(None)


def get_all_ncaab_teams():
    all_teams = []
    teams = Teams("2022")
    for team in teams._teams:
        all_teams.append(team._abbreviation)

    return all_teams


def test_player_with_no_data_happy_path():
    roster = Roster('Gonzaga')

    for player in roster.players:
        if player.player_id == "colby-brooks-1":
            assert player._player_data == {}
            assert player("2021-22").points == 0
            assert player("2021-22").minutes_played == 0
            assert player("2021-22").steals == 0


def test_player_incorrect_year():
    roster = Roster('Michigan')

    for player in roster.players:
        assert player("2921-2922").points == 0


def test_player_with_no_data_all_teams():
    all_teams = get_all_ncaab_teams()

    for i in range(len(all_teams)):
        if i % 80 == 0:
            roster = Roster(all_teams[i])
            for player in roster.players:
                if player._player_data == {}:
                    assert player("2021-22").points == 0
                    assert player("2021-22").minutes_played == 0
                    assert player("2021-22").steals == 0


class TestNCAABPlayer:
    def setup_method(self):
        flexmock(AbstractPlayer) \
            .should_receive('_parse_player_data') \
            .and_return(None)
        flexmock(Player) \
            .should_receive('_pull_player_data') \
            .and_return(None)
        flexmock(Player) \
            .should_receive('_find_initial_index') \
            .and_return(None)

    def test_no_int_return_default_value_abstract_class(self):
        mock_field_goals = PropertyMock(return_value=[''])
        mock_index = PropertyMock(return_value=0)
        player = Player(None)
        type(player)._field_goals = mock_field_goals
        type(player)._index = mock_index

        result = player.field_goals

        assert result is None

    def test_no_float_returns_default_value_abstract_class(self):
        mock_percentage = PropertyMock(return_value=[''])
        mock_index = PropertyMock(return_value=0)
        player = Player(None)
        type(player)._field_goal_percentage = mock_percentage
        type(player)._index = mock_index

        result = player.field_goal_percentage

        assert result is None

    def test_no_int_return_default_value_player_class(self):
        mock_games = PropertyMock(return_value=[''])
        mock_index = PropertyMock(return_value=0)
        player = Player(None)
        type(player)._games_played = mock_games
        type(player)._index = mock_index

        result = player.games_played

        assert result is None

    def test_no_float_returns_default_value_player_class(self):
        mock_player_efficiency_rating = PropertyMock(return_value=[''])
        mock_index = PropertyMock(return_value=0)
        player = Player(None)
        type(player)._player_efficiency_rating = mock_player_efficiency_rating
        type(player)._index = mock_index

        result = player.player_efficiency_rating

        assert result is None

    @patch('requests.get', side_effect=mock_pyquery)
    def test_invalid_url_returns_none(self, *args, **kwargs):
        mock_id = PropertyMock(return_value='BAD')
        player = Player(None)
        type(player)._player_id = mock_id

        result = player._retrieve_html_page()

        assert result is None

    def test_cleanup_of_none_returns_default(self):
        result = _cleanup(None)

        assert result == ''

    def test_cleanup_of_none_returns_default_for_player(self):
        result = _cleanup_player(None)

        assert result == ''

    def test_player_with_no_stats(self):
        player = Player(None)
        result = player._combine_season_stats(None, None, {})

        assert result == {}

    def test_player_with_no_weight_returns_none(self):
        mock_weight = PropertyMock(return_value=None)
        player = Player(None)
        type(player)._weight = mock_weight

        result = player.weight

        assert result is None

    # def test_player_with_no_data(self, create_player, create_roster):
    # roster = Roster('Gonzaga')
    #
    # for player in roster.players:
    #     if player.player_id == "colby-brooks-1":
    #         print(player.points)
    #         assert player.points == 0
    #         assert player.minutes_played == 0

    # for player in create_roster.players:
    #     print(player.player_id)
    #     print(player.points)

    # print(create_player.player_id)
    #
    # print(create_player.points)

    # assert 1 == 1

    # player = Player("colby-brooks-1")
    # print(player._player_id)
    # print(player._position)
    # print(player.points)
