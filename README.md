# django-website
example of django website with postgresql

# How to run#
create a .env file with enviroments
like

POSTGRES_DB=django
POSTGRES_USER=djangouser
POSTGRES_PASSWORD=teste123
DJANGO_SECRET_KEY=django-insecure-c0xu$8sld8-^3tr&@b6ie_%5td_e34cb1t^4s4ww0_g77bp50+

exec docker-compose to create your virtual envirement with 
docker-compose -f docker/docker-compose.yml up