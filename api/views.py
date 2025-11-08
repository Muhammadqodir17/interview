import requests
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
second_part = ""


class FinalAnswerViewSet(ViewSet):
    def get_second_part(self, request, *args, **kwargs):
        global second_part
        data = request.data
        second_part = data.get('part2')
        return Response(data={"ok": True}, status=status.HTTP_201_CREATED)

    def get_final_answer(self, request, *args, **kwargs):
        global second_part
        payload = {
            "msg": "Salom",
            "url": "https://416e62d7e453.ngrok-free.app/api/v1/api/get_second_part/"
        }
        response = requests.post("https://test.icorp.uz/interview.php", json=payload).json()
        first_part = response.get('part1')
        final_code = first_part + second_part
        result = requests.get(f"https://test.icorp.uz/interview.php?code={final_code}")
        return Response(
            data={
                'part1': first_part,
                'part2': second_part,
                'part1 + part2': final_code,
                'result': result,
            },
            status=status.HTTP_200_OK
        )
