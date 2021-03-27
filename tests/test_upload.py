import cv2
import numpy as np

# incomplete

def test_upload(app,client):
    blank_image = cv2.imread("sudoku.png")

    data = {
        
        'img': blank_image


    }
    
    ch = client.post('/home',buffered=True,
                     content_type='multipart/form-data',
                     data=data)

    assert ch.status_code == 200