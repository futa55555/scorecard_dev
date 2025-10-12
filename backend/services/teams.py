# backend/services/teams.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_team_list(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None
) -> list[schemas.TeamListItem]:
    """
    チーム一覧を取得
    """
    team_list = cruds.get_team_list(db, category_id, league_id)

    adapter = TypeAdapter(list[schemas.TeamListItem])
    return adapter.validate_python(team_list)


def get_team_list_with_page(
    db: Session,
    current_page: int,
    limit: int,
    category_id: int | None = None,
    league_id: int | None = None
) -> schemas.TeamListWithPage:
    """
    ページ付きのチーム一覧を取得
    """
    team_list, team_total_count = cruds.get_team_list_with_page(db, current_page, limit, category_id, league_id)

    adapter = TypeAdapter(list[schemas.TeamListItem])
    teams = adapter.validate_python(team_list)

    return schemas.TeamListWithPage(
        teams=teams,
        current_page=current_page,
        total_page=(team_total_count // limit + 1)
    )


def get_team_detail(
    db: Session,
    team_id: int
) -> schemas.TeamDetail:
    """
    チームの詳細情報を取得
    """
    tmp_team_detail = cruds.get_team_detail(db, team_id)

    active_people = []
    for person_profile in tmp_team_detail.person_profiles:
        active_people.append(
            schemas.PersonListItem(
                person_id=person_profile.person.id,
                last_name=person_profile.person.last_name,
                first_name=person_profile.person.first_name,
                middle_name=person_profile.person.middle_name,
                prefecture=person_profile.person.prefecture,
                person_profiles=person_profile.person.person_profiles,
                player_position=person_profile.person.player_position
            )
        )

    game_dict = {}
    for game in (tmp_team_detail.games_as_top_team or []) + (tmp_team_detail.games_as_bottom_team or []):
        game_dict[game.game_id] = game
    games = list(game_dict.values())

    return schemas.TeamDetail(
        team_id=tmp_team_detail.team_id,
        name=tmp_team_detail.name,
        short_name=tmp_team_detail.short_name,
        prefecture=tmp_team_detail.prefecture,
        chief_admin_user=tmp_team_detail.chief_admin_user,
        league=tmp_team_detail.league,
        categories=tmp_team_detail.categories,
        locations=tmp_team_detail.locations,
        tournaments=tmp_team_detail.tournaments,
        admin_users=tmp_team_detail.admin_users,
        active_people=active_people,
        games=games
    )
