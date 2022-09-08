git datasets/normalized_delta/*
git commit -m ".: AIRFLOW UPDATE $(date +'%d-%m-%Y') :."
git push origin dev
git add src/api/v2/*
git commit -m ".: AIRFLOW UPDATE $(date +'%d-%m-%Y') :."
git push origin gh-pages
