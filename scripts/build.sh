source ./scripts/ambiente.sh

docker build \
-f ./dockerfile \
--build-arg TAG=$VERSION \
-t $DOCKER_HUB_REPO/$PROYECTO:$VERSION .
