from app import schemas
import pytest

def test_get_all_posts(authorized_client, test_post):
    res = authorized_client.get("/posts/")

    def validate(post):
        post['votes'] = post.get('votes', 0)  # Adiciona votos com valor padrão 0
        return schemas.PostOut(**post)

    posts_map = map(validate, res.json())
    posts_list = list(posts_map)

    assert len(res.json()) == len(test_post)
    assert res.status_code == 200
    assert posts_list[0].id == test_post[0].id

def test_unauthorized_user_get_all_posts(client, test_post):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_post(client, test_post):
    res = client.get(f"/posts/{test_post[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_post):
    res = authorized_client.get(f"/posts/88888")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_post):
    res = authorized_client.get(f"/posts/{test_post[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.id == test_post[0].id
    assert post.content == test_post[0].content
    assert post.content == test_post[0].content

@pytest.mark.parametrize("title, content, published", [
    ("Awesome new title", "awesome new content", True),
    ("favrite food", " favorite new content", True),
    ("Tallest man", " new content", True),
])
def test_create_post(authorized_client, test_user, test_post, title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})

    created_post =schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']

def test_create_post_default_published_true(authorized_client, test_user, test_post):
    res = authorized_client.post("/posts/", json={"title": "some title", "content": "contehdvhdjvdnt"})

    created_post =schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "some title"
    assert created_post.content == "contehdvhdjvdnt"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']
    
def test_unauthorized_user_create_post(client, test_post, test_user):
    res = client.post(f"/posts/", json={"title": "some title", "content": "contehdvhdjvdnt"})
    assert res.status_code == 401


def test_unauthorized_user_delete_post(client, test_user, test_post):
    res = client.delete(
        f"/posts/{test_post[0].id}"
    )

    assert res.status_code == 401

def test_delete_post_sucess(authorized_client, test_user, test_post):
    res = authorized_client.delete(
        f"/posts/ {test_post[0].id}"
    )
    assert res.status_code == 204

def test_delete_post_non_exist(client, test_user, test_post, authorized_client):
    res = authorized_client.delete(f"/posts/80000")
    assert res.status_code == 404

def test_delete_other_user_post(authorized_client, test_user, test_post):
    res = authorized_client.delete(
        f"/posts/{test_post[3].id}"
    )
    assert res.status_code == 403


def test_update_post(authorized_client, test_user, test_post):
    data = {
        "title": "updated post",
        "content": "updated content",
        "id": test_post[0].id
    }

    res = authorized_client.put(f"/posts/{test_post[0].id}", json=data)

    update_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert update_post.title == data['title']
    assert update_post.content == data['content']
    
def test_update_other_user_post(authorized_client, test_user, test_user2, test_post):
    data = {
        "title": "updated post",
        "content": "updated content",
        "id": test_post[0].id
    }
    res = authorized_client.put(f"/posts/{test_post[3].id}", json=data)
    assert res.status_code == 403

def test_unauthorized_user_update_post(client, test_user, test_post):
    res = client.put(
        f"/posts/{test_post[0].id}"
    )

    assert res.status_code == 401

def test_update_post_non_exist(client, test_user, test_post, authorized_client):
    data = {
    "title": "updated post",
    "content": "updated content",
    "id": test_post[0].id
    }

    res = authorized_client.put(f"/posts/80000", json=data)
    assert res.status_code == 404

