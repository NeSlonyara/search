if [ -z "$1" ]; then
    echo "Использование: $0 <option>"
    echo "Опции: search 1 | search 2 | search 3"
    exit 1
fi

python3 /home/ultrakaller/Рабочий стол/project-python/SEARCH/search.py "$1"