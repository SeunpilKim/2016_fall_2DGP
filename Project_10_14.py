from pico2d import *
import math
import random
open_canvas()
xdir , ydir = 1,0
xdir_p,ydir_p = 1,0
map = load_image('Map1.png')
class Boy:
    def __init__(self):
        self.x,self.y = 400,300
        self.frame = 0
        self.image = load_image('Character.png')

    def update(self):
        global xdir
        global ydir
        self.frame = (self.frame + 1) % 3
        self.dir_x = xdir
        self.dir_y = ydir
        self.x = self.x + (self.dir_x * 5)
        self.y = self.y + (self.dir_y * 5)
        #왼쪽으로 걸어갈때 충돌체크
        if self.y > 273 and self.y < 419 and self.x > 458 and self.x < 473 and xdir == -1 and ydir == 0:
            self.x = 473
        if self.y > 479 and self.y < 572 and self.x > 458 and self.x < 473 and xdir == -1 and ydir == 0:
            self.x = 473
        if self.y > 572 and self.y < 617 and self.x > 410 and self.x < 425 and xdir == -1 and ydir == 0:
            self.x = 425
        if self.y > 562 and self.y < 600 and self.x > 515 and self.x < 530 and xdir == -1 and ydir == 0:
            self.x = 530
        if self.y > 562 and self.y < 600 and self.x > 664 and self.x < 679 and xdir == -1 and ydir == 0:
            self.x = 679
        if self.y > 489 and self.y < 527 and self.x > 617 and self.x < 632 and xdir == -1 and ydir == 0:
            self.x = 632
        if self.y > 476 and self.y < 540 and self.x > 577 and self.x < 592 and xdir == -1 and ydir == 0:
            self.x = 592
        if self.y > 476 and self.y < 617 and self.x > 693 and self.x < 708 and xdir == -1 and ydir == 0:
            self.x = 708
        if self.y > 374 and self.y < 389 and self.x > 740 and self.x < 755 and xdir == -1 and ydir == 0:
            self.x = 755
        if self.y > 271 and self.y < 309 and self.x > 740 and self.x < 755 and xdir == -1 and ydir == 0:
            self.x = 755
        if self.y > 325 and self.y < 340 and self.x > 38 and self.x < 53 and xdir == -1 and ydir == 0:
            self.x = 53
        if self.y > 273 and self.y < 369 and self.x > 350 and self.x < 365 and xdir == -1 and ydir == 0:
            self.x = 365
        if self.y > 369 and self.y < 464 and self.x > 319 and self.x < 334 and xdir == -1 and ydir == 0:
            self.x = 334
        if self.y > 464 and self.y < 517 and self.x > 298 and self.x < 306 and xdir == -1 and ydir == 0:
            self.x = 306
        if self.y > 557 and self.y < 617 and self.x > 298 and self.x < 306 and xdir == -1 and ydir == 0:
            self.x = 306
        if self.y > 0 and self.y < 136 and self.x > 298 and self.x < 306 and xdir == -1 and ydir == 0:
            self.x = 306
        if self.y > 0 and self.y < 136 and self.x > 496 and self.x < 504 and xdir == -1 and ydir == 0:
            self.x = 504
        if self.y > 136 and self.y < 156 and self.x > 479 and self.x < 487 and xdir == -1 and ydir == 0:
            self.x = 487
        if self.y > 46 and self.y < 96 and self.x > 430 and self.x < 438 and xdir == -1 and ydir == 0:
            self.x = 438
        if self.y > 431 and self.y < 617 and self.x > 190 and self.x < 198 and xdir == -1 and ydir == 0:
            self.x = 198
        if self.y > 147 and self.y < 337 and self.x > 190 and self.x < 198 and xdir == -1 and ydir == 0:
            self.x = 198
        if self.y > 229 and self.y < 269 and self.x > 134 and self.x < 142 and xdir == -1 and ydir == 0:
            self.x = 142
        if self.y > 431 and self.y < 561 and self.x > 135 and self.x < 145 and xdir == -1 and ydir == 0:
            self.x = 145
        if self.y > 135 and self.y < 150 and self.x > 369 and self.x < 377 and xdir == -1 and ydir == 0:
            self.x = 377
        if self.x < 0 and xdir == -1:
            xdir = 1
        #오른쪽으로 걸어갈때 충돌체크
        if self.y > 273 and self.y < 419 and self.x > 438 and self.x < 453 and xdir == 1 and ydir == 0:
            self.x = 443
        if self.y > 433 and self.y < 561 and self.x > 34 and self.x < 49 and xdir == 1 and ydir == 0:
            self.x = 39
        if self.y > 433 and self.y < 617 and self.x > 166 and self.x < 181 and xdir == 1 and ydir == 0:
            self.x = 171
        if self.y > 325 and self.y < 340 and self.x > 89 and self.x < 104 and xdir == 1 and ydir == 0:
            self.x = 94
        if self.y > 149 and self.y < 325 and self.x > 166 and self.x < 181 and xdir == 1 and ydir == 0:
            self.x = 171
        if self.y > 232 and self.y < 274 and self.x > 34 and self.x < 49 and xdir == 1 and ydir == 0:
            self.x = 39
        if self.y > 0 and self.y < 160 and self.x > 274 and self.x < 289 and xdir == 1 and ydir == 0:
            self.x = 279
        if self.y > 272 and self.y < 514 and self.x > 274 and self.x < 289 and xdir == 1 and ydir == 0:
            self.x = 279
        if self.y > 272 and self.y < 514 and self.x > 274 and self.x < 289 and xdir == 1 and ydir == 0:
            self.x = 279
        if self.y > 557 and self.y < 617 and self.x > 274 and self.x < 289 and xdir == 1 and ydir == 0:
            self.x = 279
        if self.y > 557 and self.y < 617 and self.x > 317 and self.x < 332 and xdir == 1 and ydir == 0:
            self.x = 322
        if self.y > 46 and self.y < 98 and self.x > 351 and self.x < 366 and xdir == 1 and ydir == 0:
            self.x = 356
        if self.y > 137 and self.y < 152 and self.x > 394 and self.x < 409 and xdir == 1 and ydir == 0:
            self.x = 399
        if self.y > 475 and self.y < 556 and self.x > 439 and self.x < 454 and xdir == 1 and ydir == 0:
            self.x = 444
        if self.y > 558 and self.y < 600 and self.x > 489 and self.x < 504 and xdir == 1 and ydir == 0:
            self.x = 494
        if self.y > 474 and self.y < 536 and self.x > 513 and self.x < 528 and xdir == 1 and ydir == 0:
            self.x = 518
        if self.y > 488 and self.y < 530 and self.x > 591 and self.x < 606 and xdir == 1 and ydir == 0:
            self.x = 596
        if self.y > 495 and self.y < 537 and self.x > 655 and self.x < 670 and xdir == 1 and ydir == 0:
            self.x = 660
        if self.y > 563 and self.y < 605 and self.x > 640 and self.x < 655 and xdir == 1 and ydir == 0:
            self.x = 645
        if self.y > 535 and self.y < 617 and self.x > 679 and self.x < 694 and xdir == 1 and ydir == 0:
            self.x = 684
        if self.y > 470 and self.y < 500 and self.x > 679 and self.x < 694 and xdir == 1 and ydir == 0:
            self.x = 684
        if self.y > 374 and self.y < 389 and self.x > 493 and self.x < 508 and xdir == 1 and ydir == 0:
            self.x = 498
        if self.y > 268 and self.y < 310 and self.x > 493 and self.x < 508 and xdir == 1 and ydir == 0:
            self.x = 498
        if self.y > 0 and self.y < 175 and self.x > 593 and self.x < 608 and xdir == 1 and ydir == 0:
            self.x = 598
        if self.y > 0 and self.y < 145 and self.x > 475 and self.x < 498 and xdir == 1 and ydir == 0:
            self.x = 480

        if self.x > 800 and xdir == 1:
            xdir = -1
        #아래로갈때 충돌체크
        if self.y > 411 and self.y < 427 and self.x > 438 and self.x < 473 and xdir == 0 and ydir == -1:
            self.y = 422
        if self.y > 553 and self.y < 569 and self.x > 45 and self.x < 134 and xdir == 0 and ydir == -1:
            self.y = 564
        if self.y > 333 and self.y < 349 and self.x > -10 and self.x < 50 and xdir == 0 and ydir == -1:
            self.y = 344
        if self.y > 333 and self.y < 349 and self.x > 102 and self.x < 193 and xdir == 0 and ydir == -1:
            self.y = 344
        if self.y > 267 and self.y < 283 and self.x > 46 and self.x < 133 and xdir == 0 and ydir == -1:
            self.y = 278
        if self.y > 51 and self.y < 67 and self.x > -10 and self.x < 285 and xdir == 0 and ydir == -1:
            self.y = 62
        if self.y > 150 and self.y < 166 and self.x > 288 and self.x < 370 and xdir == 0 and ydir == -1:
            self.y = 161
        if self.y > 150 and self.y < 166 and self.x > 407 and self.x < 490 and xdir == 0 and ydir == -1:
            self.y = 161
        if self.y > 135 and self.y < 150 and self.x > 485 and self.x < 500 and xdir == 0 and ydir == -1:
            self.y = 145
        if self.y > 365 and self.y < 381 and self.x > 321 and self.x < 352 and xdir == 0 and ydir == -1:
            self.y = 376
        if self.y > 459 and self.y < 475 and self.x > 300 and self.x < 321 and xdir == 0 and ydir == -1:
            self.y = 470
        if self.y > 513 and self.y < 527 and self.x > 285 and self.x < 300 and xdir == 0 and ydir == -1:
            self.y = 522
        if self.y > 568 and self.y < 584 and self.x > 420 and self.x < 468 and xdir == 0 and ydir == -1:
            self.y = 579
        if self.y > 597 and self.y < 613 and self.x > 503 and self.x < 524 and xdir == 0 and ydir == -1:
            self.y = 608
        if self.y > 534 and self.y < 550 and self.x > 525 and self.x < 589 and xdir == 0 and ydir == -1:
            self.y = 545
        if self.y > 525 and self.y < 541 and self.x > 605 and self.x < 630 and xdir == 0 and ydir == -1:
            self.y = 536
        if self.y > 531 and self.y < 547 and self.x > 665 and self.x < 690 and xdir == 0 and ydir == -1:
            self.y = 542
        if self.y > 382 and self.y < 398 and self.x > 504 and self.x < 751 and xdir == 0 and ydir == -1:
            self.y = 393
        if self.y > 302 and self.y < 318 and self.x > 504 and self.x < 751 and xdir == 0 and ydir == -1:
            self.y = 313
        if self.y > 163 and self.y < 179 and self.x > 603 and self.x < 810 and xdir == 0 and ydir == -1:
            self.y = 174
        if self.y > 96 and self.y < 112 and self.x > 365 and self.x < 423 and xdir == 0 and ydir == -1:
            self.y = 107
        if self.y < 0 and ydir == -1:
            ydir = 1
        #위로갈때 충돌체크
        if self.y > 265 and self.y < 281 and self.x > 450 and self.x < 465 and xdir == 0 and ydir == 1:
            self.y = 261
        if self.y > 425 and self.y < 441 and self.x > 42 and self.x < 138 and xdir == 0 and ydir == 1:
            self.y = 421
        if self.y > 425 and self.y < 441 and self.x > 175 and self.x < 200 and xdir == 0 and ydir == 1:
            self.y = 421
        if self.y > 319 and self.y < 335 and self.x > -10 and self.x < 56 and xdir == 0 and ydir == 1:
            self.y = 315
        if self.y > 319 and self.y < 335 and self.x > 99 and self.x < 186 and xdir == 0 and ydir == 1:
            self.y = 315
        if self.y > 226 and self.y < 242 and self.x > 44 and self.x < 143 and xdir == 0 and ydir == 1:
            self.y = 222
        if self.y > 143 and self.y < 159 and self.x > 176 and self.x < 191 and xdir == 0 and ydir == 1:
            self.y = 139
        if self.y > 134 and self.y < 150 and self.x > 300 and self.x < 367 and xdir == 0 and ydir == 1:
            self.y = 130
        if self.y > 134 and self.y < 150 and self.x > 406 and self.x < 483 and xdir == 0 and ydir == 1:
            self.y = 130
        if self.y > 43 and self.y < 59 and self.x > 362 and self.x < 420 and xdir == 0 and ydir == 1:
            self.y = 39
        if self.y > 268 and self.y < 284 and self.x > 283 and self.x < 355 and xdir == 0 and ydir == 1:
            self.y = 264
        if self.y > 555 and self.y < 571 and self.x > 293 and self.x < 308 and xdir == 0 and ydir == 1:
            self.y = 551
        if self.y > 555 and self.y < 571 and self.x > 331 and self.x < 458 and xdir == 0 and ydir == 1:
            self.y = 551
        if self.y > 474 and self.y < 490 and self.x > 448 and self.x < 473 and xdir == 0 and ydir == 1:
            self.y = 470
        if self.y > 558 and self.y < 574 and self.x > 497 and self.x < 522 and xdir == 0 and ydir == 1:
            self.y = 554
        if self.y > 474 and self.y < 490 and self.x > 523 and self.x < 583 and xdir == 0 and ydir == 1:
            self.y = 470
        if self.y > 499 and self.y < 515 and self.x > 609 and self.x < 634 and xdir == 0 and ydir == 1:
            self.y = 495
        if self.y > 573 and self.y < 589 and self.x > 656 and self.x < 681 and xdir == 0 and ydir == 1:
            self.y = 569
        if self.y > 500 and self.y < 516 and self.x > 672 and self.x < 697 and xdir == 0 and ydir == 1:
            self.y = 496
        if self.y > 478 and self.y < 494 and self.x > 690 and self.x < 712 and xdir == 0 and ydir == 1:
            self.y = 474
        if self.y > 375 and self.y < 391 and self.x > 503 and self.x < 759 and xdir == 0 and ydir == 1:
            self.y = 371
        if self.y > 270 and self.y < 286 and self.x > 503 and self.x < 759 and xdir == 0 and ydir == 1:
            self.y = 266


        if self.y > 600 and ydir == 1:
            ydir = -1

    def draw(self):
        if xdir == 0 and ydir == -1:
            self.image.clip_draw(self.frame*32 + 192,224,28,32,self.x,self.y)
        elif xdir == 0 and ydir == 1:
            self.image.clip_draw(self.frame * 32 + 192, 128, 28, 32, self.x, self.y)
        elif xdir == 1 and ydir == 0:
            self.image.clip_draw(self.frame * 32 + 192, 160, 28, 32, self.x, self.y)
        elif xdir == -1 and ydir == 0:
            self.image.clip_draw(self.frame * 32 + 192, 192, 28, 32, self.x, self.y)
policecount = 0
direction = [-1,1]
class police:
    def __init__(self):
        self.x, self.y = 400, 200
        self.frame = 0
        self.image = load_image('Character.png')

    def update(self):
        global xdir_p
        global ydir_p
        global police_status
        global boy
        global police
        global policecount
        global direction
        

        if math.sqrt((police.x - boy.x)*(police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) < 100:
            police_status = True

        self.frame = (self.frame + 1) % 3
        self.dir_x = xdir_p
        self.dir_y = ydir_p
        if police_status == False:
            self.x = self.x + (self.dir_x * 5)
            self.y = self.y + (self.dir_y * 5)
        if police_status == True:

            policecount += 1
            if math.sqrt((police.x - boy.x) * (police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) > 500\
                    or policecount > 30:
                police_status = False
                policecount = 0
            if boy.x > police.x and boy.y > police.y:
                self.x = self.x + math.sqrt((police.x - boy.x)*(police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y))/20
                self.y = self.y + math.sqrt((police.x - boy.x)*(police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y))/20
                xdir_p = 0
                ydir_p = 1
            if boy.x > police.x and boy.y < police.y:
                self.x = self.x + math.sqrt(
                    (police.x - boy.x) * (police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) / 20
                self.y = self.y - math.sqrt(
                    (police.x - boy.x) * (police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) / 20
                xdir_p = 1
                ydir_p = 0
            if boy.x < police.x and boy.y > police.y:
                self.x = self.x - math.sqrt(
                    (police.x - boy.x) * (police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) / 20
                self.y = self.y + math.sqrt(
                    (police.x - boy.x) * (police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) / 20
                xdir_p = -1
                ydir_p = 0
            if boy.x < police.x and boy.y < police.y:
                self.x = self.x - math.sqrt(
                    (police.x - boy.x) * (police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) / 20
                self.y = self.y - math.sqrt(
                    (police.x - boy.x) * (police.x - boy.x) + (police.y - boy.y) * (police.y - boy.y)) / 20
                xdir_p = 0
                ydir_p = -1

        #왼쪽으로 걸어갈때 충돌체크
        if self.y > 273 and self.y < 419 and self.x > 458 and self.x < 473 :
            self.x = 473
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 479 and self.y < 572 and self.x > 458 and self.x < 473 :
            self.x = 473
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 572 and self.y < 617 and self.x > 410 and self.x < 425 :
            self.x = 425
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 562 and self.y < 600 and self.x > 515 and self.x < 530 :
            self.x = 530
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 562 and self.y < 600 and self.x > 664 and self.x < 679 :
            self.x = 679
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 489 and self.y < 527 and self.x > 617 and self.x < 632 :
            self.x = 632
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 476 and self.y < 540 and self.x > 577 and self.x < 592 :
            self.x = 592
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 476 and self.y < 617 and self.x > 693 and self.x < 708 :
            self.x = 708
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 374 and self.y < 389 and self.x > 740 and self.x < 755 :
            self.x = 755
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 271 and self.y < 309 and self.x > 740 and self.x < 755 :
            self.x = 755
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 325 and self.y < 340 and self.x > 38 and self.x < 53 :
            self.x = 53
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 273 and self.y < 369 and self.x > 350 and self.x < 365 :
            self.x = 365
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 369 and self.y < 464 and self.x > 319 and self.x < 334 :
            self.x = 334
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 464 and self.y < 517 and self.x > 298 and self.x < 306 :
            self.x = 306
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 557 and self.y < 617 and self.x > 298 and self.x < 306 :
            self.x = 306
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 0 and self.y < 136 and self.x > 298 and self.x < 306 :
            self.x = 306
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 0 and self.y < 136 and self.x > 496 and self.x < 504 :
            self.x = 504
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 136 and self.y < 156 and self.x > 479 and self.x < 487 :
            self.x = 487
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 46 and self.y < 96 and self.x > 430 and self.x < 438 :
            self.x = 438
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 431 and self.y < 617 and self.x > 190 and self.x < 198 :
            self.x = 198
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 147 and self.y < 337 and self.x > 190 and self.x < 198 :
            self.x = 198
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 229 and self.y < 269 and self.x > 134 and self.x < 142 :
            self.x = 142
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 431 and self.y < 561 and self.x > 135 and self.x < 145 :
            self.x = 145
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.y > 135 and self.y < 150 and self.x > 369 and self.x < 377 :
            self.x = 377
            if police_status == False:
                xdir_p = 0
                self.x += 10
                ydir_p = random.choice(direction)
        if self.x < 0 and xdir_p == -1:
            xdir_p = 1
        #오른쪽으로 걸어갈때 충돌체크
        if self.y > 273 and self.y < 419 and self.x > 438 and self.x < 453 :
            self.x = 443
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 433 and self.y < 561 and self.x > 34 and self.x < 49 :
            self.x = 39
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 433 and self.y < 617 and self.x > 166 and self.x < 181 :
            self.x = 171
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 325 and self.y < 340 and self.x > 89 and self.x < 104 :
            self.x = 94
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 149 and self.y < 325 and self.x > 166 and self.x < 181 :
            self.x = 171
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 232 and self.y < 274 and self.x > 34 and self.x < 49 :
            self.x = 39
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 0 and self.y < 160 and self.x > 274 and self.x < 289 :
            self.x = 279
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 272 and self.y < 514 and self.x > 274 and self.x < 289 :
            self.x = 279
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 272 and self.y < 514 and self.x > 274 and self.x < 289 :
            self.x = 279
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 557 and self.y < 617 and self.x > 274 and self.x < 289 :
            self.x = 279
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 557 and self.y < 617 and self.x > 317 and self.x < 332 :
            self.x = 322
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 46 and self.y < 98 and self.x > 351 and self.x < 366 :
            self.x = 356
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 137 and self.y < 152 and self.x > 394 and self.x < 409 :
            self.x = 399
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 475 and self.y < 556 and self.x > 439 and self.x < 454 :
            self.x = 444
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 558 and self.y < 600 and self.x > 489 and self.x < 504 :
            self.x = 494
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 474 and self.y < 536 and self.x > 513 and self.x < 528 :
            self.x = 518
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 488 and self.y < 530 and self.x > 591 and self.x < 606 :
            self.x = 596
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 495 and self.y < 537 and self.x > 655 and self.x < 670 :
            self.x = 660
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 563 and self.y < 605 and self.x > 640 and self.x < 655 :
            self.x = 645
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 535 and self.y < 617 and self.x > 679 and self.x < 694 :
            self.x = 684
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 470 and self.y < 500 and self.x > 679 and self.x < 694 :
            self.x = 684
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 374 and self.y < 389 and self.x > 493 and self.x < 508 :
            self.x = 498
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 268 and self.y < 310 and self.x > 493 and self.x < 508 :
            self.x = 498
            if police_status == False:
                xdir_p = 0
                self.x -= 10
                ydir_p = random.choice(direction)
        if self.y > 0 and self.y < 175 and self.x > 593 and self.x < 608 :
            self.x = 598
            if police_status == False:
                xdir_p = 0
                ydir_p = random.choice(direction)
                self.x -= 10
        if self.y > 0 and self.y < 145 and self.x > 475 and self.x < 498 :
            self.x = 480
            if police_status == False:
                xdir_p = 0
                ydir_p = random.choice(direction)
                self.x -= 10

        if self.x > 800 and xdir_p == 1:
            xdir_p = -1
        #아래로갈때 충돌체크
        if self.y > 411 and self.y < 427 and self.x > 438 and self.x < 473:
            self.y = 422
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 553 and self.y < 569 and self.x > 45 and self.x < 134 :
            self.y = 564
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 333 and self.y < 349 and self.x > -10 and self.x < 50 :
            self.y = 344
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 333 and self.y < 349 and self.x > 102 and self.x < 193 :
            self.y = 344
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 267 and self.y < 283 and self.x > 46 and self.x < 133 :
            self.y = 278
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 51 and self.y < 67 and self.x > -10 and self.x < 285 :
            self.y = 62
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 150 and self.y < 166 and self.x > 288 and self.x < 370 :
            self.y = 161
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 150 and self.y < 166 and self.x > 407 and self.x < 490 :
            self.y = 161
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 135 and self.y < 150 and self.x > 485 and self.x < 500 :
            self.y = 145
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 365 and self.y < 381 and self.x > 321 and self.x < 352 :
            self.y = 376
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 459 and self.y < 475 and self.x > 300 and self.x < 321 :
            self.y = 470
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 513 and self.y < 527 and self.x > 285 and self.x < 300 :
            self.y = 522
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 568 and self.y < 584 and self.x > 420 and self.x < 468 :
            self.y = 579
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 597 and self.y < 613 and self.x > 503 and self.x < 524 :
            self.y = 608
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 534 and self.y < 550 and self.x > 525 and self.x < 589 :
            self.y = 545
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 525 and self.y < 541 and self.x > 605 and self.x < 630 :
            self.y = 536
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 531 and self.y < 547 and self.x > 665 and self.x < 690 :
            self.y = 542
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 382 and self.y < 398 and self.x > 504 and self.x < 751 :
            self.y = 393
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 302 and self.y < 318 and self.x > 504 and self.x < 751:
            self.y = 313
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 163 and self.y < 179 and self.x > 603 and self.x < 810 :
            self.y = 174
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y > 96 and self.y < 112 and self.x > 365 and self.x < 423 :
            self.y = 107
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y += 10
        if self.y < 0 and ydir_p == -1:
            ydir_p = 1
        #위로갈때 충돌체크
        if self.y > 265 and self.y < 281 and self.x > 450 and self.x < 465 :
            self.y = 261
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 425 and self.y < 441 and self.x > 42 and self.x < 138 :
            self.y = 421
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 425 and self.y < 441 and self.x > 175 and self.x < 200 :
            self.y = 421
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 319 and self.y < 335 and self.x > -10 and self.x < 56 :
            self.y = 315
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 319 and self.y < 335 and self.x > 99 and self.x < 186 :
            self.y = 315
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 226 and self.y < 242 and self.x > 44 and self.x < 143 :
            self.y = 222
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 143 and self.y < 159 and self.x > 176 and self.x < 191 :
            self.y = 139
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 134 and self.y < 150 and self.x > 300 and self.x < 367 :
            self.y = 130
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 134 and self.y < 150 and self.x > 406 and self.x < 483 :
            self.y = 130
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 43 and self.y < 59 and self.x > 362 and self.x < 420 :
            self.y = 39
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 268 and self.y < 284 and self.x > 283 and self.x < 355 :
            self.y = 264
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 555 and self.y < 571 and self.x > 293 and self.x < 308 :
            self.y = 551
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 555 and self.y < 571 and self.x > 331 and self.x < 458 :
            self.y = 551
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 474 and self.y < 490 and self.x > 448 and self.x < 473 :
            self.y = 470
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 558 and self.y < 574 and self.x > 497 and self.x < 522 :
            self.y = 554
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 474 and self.y < 490 and self.x > 523 and self.x < 583 :
            self.y = 470
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 499 and self.y < 515 and self.x > 609 and self.x < 634 :
            self.y = 495
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 573 and self.y < 589 and self.x > 656 and self.x < 681 :
            self.y = 569
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 500 and self.y < 516 and self.x > 672 and self.x < 697 :
            self.y = 496
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 478 and self.y < 494 and self.x > 690 and self.x < 712 :
            self.y = 474
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 375 and self.y < 391 and self.x > 503 and self.x < 759 :
            self.y = 371
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10
        if self.y > 270 and self.y < 286 and self.x > 503 and self.x < 759 :
            self.y = 266
            if police_status == False:
                xdir_p = random.choice(direction)
                ydir_p = 0
                self.y -= 10


        if self.y > 600 and ydir_p == 1:
            ydir_p = -1

    def draw(self):
        if xdir_p == 0 and ydir_p == -1:
            self.image.clip_draw(self.frame*32 ,96,28,32,self.x,self.y)
        elif xdir_p == 0 and ydir_p == 1:
            self.image.clip_draw(self.frame * 32, 0, 28, 32, self.x, self.y)
        elif xdir_p == 1 and ydir_p == 0:
            self.image.clip_draw(self.frame * 32, 32, 28, 32, self.x, self.y)
        elif xdir_p == -1 and ydir_p == 0:
            self.image.clip_draw(self.frame * 32, 64, 28, 32, self.x, self.y)

police_status = False
game_status = True
boy = Boy()
police = police()
def check():
    global boy
    global police
    global xdir_p
    global ydir_p
    if police.x <= boy.x:
        xdir_p = 1
        ydir_p = 1
    if police.x >= boy.x:
        xdir_p = -1
        ydir_p = 1
    if police.y >= boy.y:
        xdir_p = 1
        ydir_p = -1
    if police.y <= boy.y:
        xdir_p = 1
        ydir_p = 1

def handle_events():
    global game_status
    global boy
    global xdir
    global ydir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_status = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            xdir = 1
            ydir = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            xdir = -1
            ydir = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            xdir = 0
            ydir = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            xdir = 0
            ydir = -1


while game_status:
    #if police_status == True:
     #   check()
    handle_events()
    boy.update()

    police.update()
    clear_canvas()
    map.draw(400,300)
    boy.draw()
    police.draw()
    update_canvas()
    delay(0.05)


close_canvas()

