# deploy.sh

quarto render

rm -rf public
git clone git@github.com:antcallabck/antcallabck.github.io.git public
cp -r _site/* public/
cd public
git add .
git commit -m "Deploy $(date)"
git push origin main
cd ..
rm -rf public
