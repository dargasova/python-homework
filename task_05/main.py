organizer = input("Ваше имя (например, Ольга): ")
print(f"Здравствуйте, {organizer}! Открываем зрительское голосование")

movies = ["дюна", "аватар", "матрица", "интерстеллар", "шрек"]
votes = {movie: 0 for movie in movies}
voters = set()
liked_by_everyone = set(movies)
print(f"Фильмы в программе фестиваля: {', '.join(movies)}")

while True:
    viewer = input('\nИмя зрителя, например Аня (или "стоп"): ').strip()
    if viewer.lower() == "стоп":
        break

    viewer_key = viewer.lower()
    if viewer_key in voters:
        print(f"{viewer}, вы уже голосовали, второй голос не засчитан")
        continue

    voters.add(viewer_key)
    raw_choices = input(
        "Выберите через запятую: дюна, аватар, матрица, интерстеллар, шрек: "
    )
    choices = {choice.strip().lower() for choice in raw_choices.split(",")}
    valid_choices = choices & set(movies)

    for choice in choices - set(movies):
        if choice:
            print(f"Фильма «{choice}» нет в программе, голос не засчитан")
    for movie in valid_choices:
        votes[movie] += 1

    liked_by_everyone &= valid_choices
    print(f"Спасибо, {viewer}! Засчитано голосов: {len(valid_choices)}")

print("\nИтоги голосования")
print(f"Проголосовало зрителей: {len(voters)}")
for movie in movies:
    print(f"{movie} - {votes[movie]}")

winner = max(movies, key=lambda movie: votes[movie])
print(f"Победитель: {winner} ({votes[winner]})")

common_movies = [movie for movie in movies if movie in liked_by_everyone]
if voters and common_movies:
    print(f"Понравились всем: {', '.join(common_movies)}")
else:
    print("Фильмов, понравившихся всем, нет")

movies_without_votes = set(movies) - {movie for movie, count in votes.items() if count > 0}
print(
    "Не выбрал никто: "
    + (", ".join(movie for movie in movies if movie in movies_without_votes) or "таких фильмов нет")
)
print(f"\nДо свидания, {organizer}!")
