from api.serializers import PhotoSerializer


def store_data(data):
    serializer = PhotoSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    print(f"{len(data)} objects has been successfully stored in database.")
