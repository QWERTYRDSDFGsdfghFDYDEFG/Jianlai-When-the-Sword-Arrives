# Sample Prompts

Use these as inference baselines after training or as strict reference prompts before training.

## 陈平安 (`cpa`)

Positive:

`cpa_person, 陈平安, male, age 20-22, slim long face, stable eyebrow-eye-nose-mouth proportions, calm, reliable, restrained, not idol-like, strict identity lock, same face as anchor images, Song-dynasty fantasy visual novel, restrained expression, real age feeling, real clothing structure`

Negative:

`wider jaw, bigger eyes, boyish look, older face, idol male lead styling`

## 崔东山 (`cds`)

Positive:

`cds_person, 崔东山, male, age 18-21, narrow slightly long face, slightly narrow long eyes, small brow mark, restrained scholar temperament, not template handsome, strict identity lock, same face as anchor images, Song-dynasty fantasy visual novel, restrained expression, real age feeling, real clothing structure`

Negative:

`wider face, rounder jaw, bigger eyes, idol handsome face, generic ancient-costume male lead`

## 李宝瓶 (`lbp`)

Positive:

`lbp_person, 李宝瓶, female child, age 12, straight bangs, high double buns, small bell ornaments, precise ribbon shape, delicate face, short winter outer jacket with fur collar, strict identity lock, same face as anchor images, Song-dynasty fantasy visual novel, restrained expression, real age feeling, real clothing structure`

Negative:

`too young toddler look, older teenager look, long robe silhouette, missing bells, wrong ribbon shape`

## 裴钱 (`pq`)

Positive:

`pq_person, 裴钱, female child, stable face identity from master image, same person across poses and scenes, strict identity lock, same face as anchor images, Song-dynasty fantasy visual novel, restrained expression, real age feeling, real clothing structure`

Negative:

`identity drift, older face, idolized styling`

## Multi-character scene rule

Do not rely on one fresh prompt to invent two stable faces at once.

Recommended route:

1. Generate or select each character from their own locked identity workflow.
2. Keep scene generation responsible for space, action, and lighting.
3. Treat the characters as hard anchors during compositing or scene redraws.

