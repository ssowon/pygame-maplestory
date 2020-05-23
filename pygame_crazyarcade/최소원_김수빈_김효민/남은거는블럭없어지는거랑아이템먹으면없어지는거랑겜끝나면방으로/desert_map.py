import pygame
import gameimage


def stop_block():  # 안움직이는 블럭
    uncrushed_block1 = gameimage.stop_block('./image/사막/보급 (2).png', 2, 2)
    uncrushed_block2 = gameimage.stop_block('./image/사막/보급 (2).png', 10, 2)
    uncrushed_block3 = gameimage.stop_block('./image/사막/보급 (2).png', 6, 4)
    uncrushed_block4 = gameimage.stop_block('./image/사막/보급 (2).png', 2, 8)
    uncrushed_block5 = gameimage.stop_block('./image/사막/보급 (2).png', 10, 12)
    uncrushed_block6 = gameimage.stop_block('./image/사막/돌.png', 6, 2)
    uncrushed_block7 = gameimage.stop_block('./image/사막/돌.png', 8, 2)
    uncrushed_block8 = gameimage.stop_block('./image/사막/돌.png', 14, 2)
    uncrushed_block9 = gameimage.stop_block('./image/사막/돌.png', 2, 4)
    uncrushed_block10 = gameimage.stop_block('./image/사막/돌.png', 10, 4)
    uncrushed_block11 = gameimage.stop_block('./image/사막/돌.png', 14, 4)
    uncrushed_block12 = gameimage.stop_block('./image/사막/돌.png', 6, 6)
    uncrushed_block13 = gameimage.stop_block('./image/사막/돌.png', 6, 10)
    uncrushed_block14 = gameimage.stop_block('./image/사막/돌.png', 10, 10)
    uncrushed_block15 = gameimage.stop_block('./image/사막/돌.png', 6, 12)
    uncrushed_block16 = gameimage.stop_block('./image/사막/돌.png', 12, 12)
    uncrushed_block17 = gameimage.stop_block('./image/사막/보급 (1).png', 4, 4)
    uncrushed_block18 = gameimage.stop_block('./image/사막/보급 (1).png', 14, 8)
    uncrushed_block19 = gameimage.stop_block('./image/사막/보급 (1).png', 2, 12)
    uncrushed_block20 = gameimage.stop_block('./image/사막/보급 (1).png', 4, 12)
    uncrushed_block21 = gameimage.stop_block('./image/사막/선인장 (1).png', 8, 4)
    uncrushed_block22 = gameimage.stop_block('./image/사막/선인장 (1).png', 6, 8)
    uncrushed_block23 = gameimage.stop_block('./image/사막/선인장 (1).png', 12, 8)
    uncrushed_block24 = gameimage.stop_block('./image/사막/선인장 (2).png', 12, 4)
    uncrushed_block25 = gameimage.stop_block('./image/사막/선인장 (2).png', 4, 6)
    uncrushed_block26 = gameimage.stop_block('./image/사막/선인장 (2).png', 4, 10)
    uncrushed_block27 = gameimage.stop_block('./image/사막/선인장 (2).png', 8, 10)
    uncrushed_block28 = gameimage.stop_block('./image/사막/선인장 (2).png', 12, 10)
    uncrushed_block29 = gameimage.stop_block('./image/사막/텐트노란.png', 4, 2)
    uncrushed_block30 = gameimage.stop_block('./image/사막/텐트노란.png', 14, 10)
    uncrushed_block31 = gameimage.stop_block('./image/사막/텐트노란.png', 8, 12)
    uncrushed_block32 = gameimage.stop_block('./image/사막/텐트빨강.png', 12, 2)
    uncrushed_block33 = gameimage.stop_block('./image/사막/텐트빨강.png', 2, 6)
    uncrushed_block34 = gameimage.stop_block('./image/사막/텐트빨강.png', 10, 6)
    uncrushed_block35 = gameimage.stop_block('./image/사막/텐트빨강.png', 14, 12)
    uncrushed_block36 = gameimage.stop_block('./image/사막/텐트파란.png', 12, 6)
    uncrushed_block37 = gameimage.stop_block('./image/사막/텐트파란.png', 4, 8)
    uncrushed_block38 = gameimage.stop_block('./image/사막/텐트파란.png', 2, 10)
    uncrushed_block39 = gameimage.stop_block('./image/사막/오아시스 (1).png', 8.5, 8)

    stop_block_Sprites = pygame.sprite.OrderedUpdates(uncrushed_block1, uncrushed_block2, uncrushed_block3,
                                                      uncrushed_block4, uncrushed_block5, uncrushed_block6,
                                                      uncrushed_block7, uncrushed_block8, uncrushed_block9,
                                                      uncrushed_block10, uncrushed_block11, uncrushed_block12,
                                                      uncrushed_block13, uncrushed_block14, uncrushed_block15,
                                                      uncrushed_block16, uncrushed_block17, uncrushed_block18,
                                                      uncrushed_block19, uncrushed_block20, uncrushed_block21,
                                                      uncrushed_block22, uncrushed_block23, uncrushed_block24,
                                                      uncrushed_block25, uncrushed_block26, uncrushed_block27,
                                                      uncrushed_block28, uncrushed_block29, uncrushed_block30,
                                                      uncrushed_block31, uncrushed_block32, uncrushed_block33,
                                                      uncrushed_block34, uncrushed_block35, uncrushed_block36,
                                                      uncrushed_block37, uncrushed_block38, uncrushed_block39)

    return stop_block_Sprites