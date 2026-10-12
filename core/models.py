from django.db import models

class Effect(models.Model):
  name = models.CharField(max_length=30, unique=True)

  def __str__(self):
    return self.name

class Card(models.Model):
  class Rarity(models.TextChoices):
    COMMON = 'Common' 
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    LEGENDARY = 'Legendary'
    MYTHIC = 'Mythic'

  class Type(models.TextChoices):
    ATTACK = 'Attack'
    DEFEND = 'Defend'
    POWER = 'Power'
    MOVE = 'Move'

  name = models.CharField(max_length=60)
  cost = models.PositiveIntegerField(default=1)
  type = models.CharField(max_length=10, choices=Type.choices, default=Type.ATTACK)
  rarity = models.CharField(max_length=10, choices=Rarity.choices, default=Rarity.COMMON)
  description = models.TextField(blank=True)
  effects = models.ManyToManyField(Effect, blank=True, related_name='cards')

  def __str__(self):
    return self.name

