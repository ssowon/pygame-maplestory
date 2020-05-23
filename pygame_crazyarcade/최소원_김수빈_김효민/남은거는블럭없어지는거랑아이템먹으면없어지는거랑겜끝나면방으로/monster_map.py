import pygame
import gameimage

def stop_block():#안움직이는 블럭
    uncrushed_block1 = gameimage.stop_block('./image/무덤/벽돌.png',1,5)
    uncrushed_block2 = gameimage.stop_block('./image/무덤/벽돌.png',1,9)
    uncrushed_block3 = gameimage.stop_block('./image/무덤/벽돌.png',2,5)
    uncrushed_block4 = gameimage.stop_block('./image/무덤/벽돌.png',2,9)
    uncrushed_block5 = gameimage.stop_block('./image/무덤/벽돌.png',5,5)
    uncrushed_block6 = gameimage.stop_block('./image/무덤/벽돌.png',5,9)
    uncrushed_block7 = gameimage.stop_block('./image/무덤/벽돌.png',6,1)
    uncrushed_block8 = gameimage.stop_block('./image/무덤/벽돌.png',6,2)
    uncrushed_block9 = gameimage.stop_block('./image/무덤/벽돌.png',6,9)
    uncrushed_block10 = gameimage.stop_block('./image/무덤/벽돌.png',6,10)
    uncrushed_block11 = gameimage.stop_block('./image/무덤/벽돌.png',6,13)
    uncrushed_block12 = gameimage.stop_block('./image/무덤/벽돌.png',10,1)
    uncrushed_block13 = gameimage.stop_block('./image/무덤/벽돌.png',10,2)
    uncrushed_block14 = gameimage.stop_block('./image/무덤/벽돌.png',10,9)
    uncrushed_block15 = gameimage.stop_block('./image/무덤/벽돌.png',10,10)
    uncrushed_block16 = gameimage.stop_block('./image/무덤/벽돌.png',10,13)
    uncrushed_block17 = gameimage.stop_block('./image/무덤/벽돌.png',11,5)
    uncrushed_block18 = gameimage.stop_block('./image/무덤/벽돌.png',11,9)
    uncrushed_block19 = gameimage.stop_block('./image/무덤/벽돌.png',14,5)
    uncrushed_block20 = gameimage.stop_block('./image/무덤/벽돌.png',14,9)
    uncrushed_block21 = gameimage.stop_block('./image/무덤/벽돌.png',15,5)
    uncrushed_block22 = gameimage.stop_block('./image/무덤/벽돌.png',15,9)
    uncrushed_block23 = gameimage.stop_block('./image/무덤/렌턴_왼쪽.png',8,5)
    uncrushed_block24 = gameimage.stop_block('./image/무덤/렌턴_오른쪽.png',9,5)
    uncrushed_block25 = gameimage.stop_block('./image/무덤/렌턴 (3).png',6,5)
    uncrushed_block26 = gameimage.stop_block('./image/무덤/렌턴 (3).png',10,5)
    uncrushed_block27 = gameimage.stop_block('./image/무덤/묘비.png',8,1)

    stop_block_Sprites = pygame.sprite.OrderedUpdates(uncrushed_block1,uncrushed_block2,uncrushed_block3,
                                                      uncrushed_block4,uncrushed_block5,uncrushed_block6,
                                                      uncrushed_block7,uncrushed_block8,uncrushed_block9,
                                                      uncrushed_block10,uncrushed_block11,uncrushed_block12,
                                                      uncrushed_block13,uncrushed_block14,uncrushed_block15,
                                                      uncrushed_block16,uncrushed_block17,uncrushed_block18,
                                                      uncrushed_block19,uncrushed_block20,uncrushed_block21,
                                                      uncrushed_block22,uncrushed_block23,uncrushed_block24,
                                                      uncrushed_block25,uncrushed_block26,uncrushed_block27)

    return stop_block_Sprites


