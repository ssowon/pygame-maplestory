import pygame
import gameimage

def stop_block():  # 안움직이는 블럭
    #안움직이는 블럭
    redhouse_block1 = gameimage.stop_block('./image/빌리지/빨간집.png',2,2)
    redhouse_block2 = gameimage.stop_block('./image/빌리지/빨간집.png',4,2)
    redhouse_block3 = gameimage.stop_block('./image/빌리지/빨간집.png',2,4)
    redhouse_block4 = gameimage.stop_block('./image/빌리지/빨간집.png',4,4)
    redhouse_block5 = gameimage.stop_block('./image/빌리지/빨간집.png',12,8)
    redhouse_block6 = gameimage.stop_block('./image/빌리지/빨간집.png',12,10)
    redhouse_block7 = gameimage.stop_block('./image/빌리지/빨간집.png',12,12)
    redhouse_block8 = gameimage.stop_block('./image/빌리지/빨간집.png',14,8)
    redhouse_block9 = gameimage.stop_block('./image/빌리지/빨간집.png',14,10)
    redhouse_block10 = gameimage.stop_block('./image/빌리지/빨간집.png',14,12)
    redhouse_block11 = gameimage.stop_block('./image/빌리지/빨간집.png',2,6)
    redhouse_block12 = gameimage.stop_block('./image/빌리지/빨간집.png',4,6)


    yellohouse_block1 = gameimage.stop_block('./image/빌리지/노란집.png',11,1)
    yellohouse_block2 = gameimage.stop_block('./image/빌리지/노란집.png',13,1)
    yellohouse_block3 = gameimage.stop_block('./image/빌리지/노란집.png',15,1)
    yellohouse_block4 = gameimage.stop_block('./image/빌리지/노란집.png',11,3)
    yellohouse_block5 = gameimage.stop_block('./image/빌리지/노란집.png',13,3)
    yellohouse_block6 = gameimage.stop_block('./image/빌리지/노란집.png',15,3)
    yellohouse_block7 = gameimage.stop_block('./image/빌리지/노란집.png',11,5)
    yellohouse_block8 = gameimage.stop_block('./image/빌리지/노란집.png',13,5)
    yellohouse_block9 = gameimage.stop_block('./image/빌리지/노란집.png',15,5)

    bluehouse_block1 = gameimage.stop_block('./image/빌리지/파란집.png',1,9)
    bluehouse_block2 = gameimage.stop_block('./image/빌리지/파란집.png',1,11)
    bluehouse_block3 = gameimage.stop_block('./image/빌리지/파란집.png',1,13)
    bluehouse_block4 = gameimage.stop_block('./image/빌리지/파란집.png',3,9)
    bluehouse_block5 = gameimage.stop_block('./image/빌리지/파란집.png',3,11)
    bluehouse_block6 = gameimage.stop_block('./image/빌리지/파란집.png',3,13)
    bluehouse_block7 = gameimage.stop_block('./image/빌리지/파란집.png',5,9)
    bluehouse_block8 = gameimage.stop_block('./image/빌리지/파란집.png',5,11)
    bluehouse_block9 = gameimage.stop_block('./image/빌리지/파란집.png',5,13)

    tree_block1 = gameimage.stop_block('./image/빌리지/나무.png',6,2)
    tree_block2 = gameimage.stop_block('./image/빌리지/나무.png',10,2)
    tree_block3 = gameimage.stop_block('./image/빌리지/나무.png',6,4)
    tree_block4 = gameimage.stop_block('./image/빌리지/나무.png',10,4)
    tree_block5 = gameimage.stop_block('./image/빌리지/나무.png',6,6)
    tree_block6 = gameimage.stop_block('./image/빌리지/나무.png',1,7)
    tree_block7 = gameimage.stop_block('./image/빌리지/나무.png',3,7)
    tree_block8 = gameimage.stop_block('./image/빌리지/나무.png',5,7)
    tree_block9 = gameimage.stop_block('./image/빌리지/나무.png',11,7)
    tree_block10 = gameimage.stop_block('./image/빌리지/나무.png',13,7)
    tree_block11 = gameimage.stop_block('./image/빌리지/나무.png',15,7)
    tree_block12 = gameimage.stop_block('./image/빌리지/나무.png',10,8)
    tree_block13 = gameimage.stop_block('./image/빌리지/나무.png',6,10)
    tree_block14 = gameimage.stop_block('./image/빌리지/나무.png',10,10)
    tree_block15 = gameimage.stop_block('./image/빌리지/나무.png',6,12)
    tree_block16 = gameimage.stop_block('./image/빌리지/나무.png',10,12)

    stop_block_Sprites = pygame.sprite.OrderedUpdates(redhouse_block1, redhouse_block2, redhouse_block3,
                                                      redhouse_block4, redhouse_block5, redhouse_block6,
                                                      redhouse_block7, redhouse_block8, redhouse_block8,
                                                      redhouse_block9, redhouse_block10, redhouse_block11,
                                                      redhouse_block12,
                                                      yellohouse_block1, yellohouse_block2, yellohouse_block3,
                                                      yellohouse_block4, yellohouse_block5, yellohouse_block6,
                                                      yellohouse_block7, yellohouse_block8, yellohouse_block9,
                                                      bluehouse_block1, bluehouse_block2, bluehouse_block3,
                                                      bluehouse_block4, bluehouse_block5, bluehouse_block6,
                                                      bluehouse_block7, bluehouse_block8, bluehouse_block9,
                                                      tree_block1, tree_block2, tree_block3, tree_block4, tree_block5,
                                                      tree_block6, tree_block7, tree_block8, tree_block9, tree_block10,
                                                      tree_block11, tree_block12, tree_block13, tree_block14, tree_block15,
                                                      tree_block16)
    return stop_block_Sprites

def nonstop_block():
    block1 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 2, 1)
    block2 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 4, 1)
    block5 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 2, 5)
    block6 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 4, 5)
    block7 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 1, 6)
    block8 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 3, 6)
    block9 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 5, 6)
    block12 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 1, 10)
    block13 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 3, 10)
    block14 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 5, 10)
    box1 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 3, 2)
    box2 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 5, 2)
    box3 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 1, 4)
    box4 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 3, 4)
    box5 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 5, 4)
    box6 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 2, 9)
    box7 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 4, 9)
    box8 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 2, 11)
    box9 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 4, 11)
    rblock3 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 4, 3)
    rblock7 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 1, 8)
    rblock8 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 3, 8)
    rblock9 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 5, 8)
    rblock12 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 3, 12)
    rblock13 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 5, 12)
    rblock14 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 4, 13)
    g1 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 2, 7)
    g2 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 4, 7)
    g3 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 7)
    g4 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 1)
    g5 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 3)
    g6 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 5)
    g7 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 9)
    g8 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 11)
    g9 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 13)
    g10 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 1)
    g11 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 3)
    g12 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 5)
    g13 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 7)
    g14 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 9)
    g15 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 11)
    g16 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 13)
    g17 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 12, 7)
    g18 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 14, 7)
    tblock1 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 12, 1)
    tblock2 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png',11, 2)
    tblock3 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 13, 2)
    tblock6 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 11, 6)
    tblock7 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 13, 6)
    tblock8 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 15, 6)
    tblock9 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 11, 8)
    tblock10 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 13, 8)
    tblock11 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 15, 8)
    tblock12 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 12, 9)
    tblock13 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 14, 9)
    tblock16 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 12, 13)
    qblock2 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 11, 4)
    qblock3 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 13, 4)
    qblock4 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 15, 4)
    qblock10 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 12,11)
    qblock11 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 14, 11)
    qbox1 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 12, 3)
    qbox2 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 14, 3)
    qbox3 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 12, 5)
    qbox4 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 14, 5)
    qbox5 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 11, 10)
    qbox6 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 13, 10)
    qbox7 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 15, 10)
    qbox8 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 11, 12)
    qbox9 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 13, 12)

    sbox1 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 2)
    sbox2 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 4)
    sbox4 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 8)
    sbox5 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 10)
    sbox6 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 12)
    sbox7 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 8, 3)
    sbox8 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 8, 6)
    sbox9 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 8, 9)
    sbox11 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 1)
    sbox13 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 5)
    sbox14 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 7)
    sbox16 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 11)
    sbox17 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 13)


    nonstop_block_Sprites = pygame.sprite.OrderedUpdates(
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,
        block1,block2,box1,box2,
        rblock3,box3,box4,box5,block5,block6,
        block7,block8,block9,rblock8,rblock9,rblock7,
        box6,box7,block12,block13,block14,box8,box9,
        rblock12,rblock13,rblock14,
        tblock1,tblock2,qbox1,qbox2,qblock2,qblock3,qblock4,tblock3,qbox3,qbox4,
        g17,g18,tblock6,tblock7,tblock8,tblock9,tblock10,tblock11,qbox5,qbox6,qbox7,
        tblock12,tblock13,qblock10,qblock11,tblock16,qbox8,qbox9,
        sbox1,sbox2,sbox4,sbox5,sbox6,sbox7,sbox8,sbox9,sbox11,sbox13,sbox14,sbox16,sbox17)

    return nonstop_block_Sprites

def item():
    item1 = gameimage.item_speed('./image/item/인라인.png', 2, 1)
    item2 = gameimage.item_ball('./image/item/물풍선.png', 12, 1)
    item5 = gameimage.item_speed('./image/item/인라인.png', 2, 5)
    item6 = gameimage.item_ball('./image/item/물풍선.png', 4, 5)
    item7 = gameimage.item_mulyak('./image/item/물약.png', 12, 13)
    item8 = gameimage.item_speed('./image/item/인라인.png', 3, 6)
    item9 = gameimage.item_ball('./image/item/물풍선.png', 5, 6)
    item11 = gameimage.item_mulyak('./image/item/물약.png', 11, 6)
    item12 = gameimage.item_speed('./image/item/인라인.png', 1, 10)
    item13 = gameimage.item_ball('./image/item/물풍선.png', 11, 18)
    item14 = gameimage.item_mulyak('./image/item/물약.png', 5, 10)
    item18 = gameimage.item_mulyak('./image/item/물약.png', 14, 9)
    item21 = gameimage.item_mulyak('./image/item/물약.png', 15, 4)
    item22 = gameimage.item_ball('./image/item/물풍선.png', 1, 8)
    item23 = gameimage.item_mulyak('./image/item/물약.png', 3, 8)
    item24 = gameimage.item_speed('./image/item/인라인.png', 5, 8)
    item27 = gameimage.item_speed('./image/item/인라인.png', 3, 12)
    item28 = gameimage.item_mulyak('./image/item/물약.png', 14, 11)
    item29 = gameimage.item_ball('./image/item/물풍선.png', 4, 13)

    item_Sprites = pygame.sprite.OrderedUpdates(item1,item2,item5,item6,item7,item8,item9,item11,item12,item13,
                                                item14,item18,item21,item22,item23,item24,item27,
                                                item28,item29)

    return item_Sprites