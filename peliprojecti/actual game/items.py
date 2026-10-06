import random
import classes

# items
grow_accel = classes.Accelerant("growth accelerator", 5, 0.5)

# crops
pumpkin = classes.Accelerant("pumpkin", 5, 0.1)
melon = classes.Accelerant("melon", 5, 0.15)
tomato = classes.Accelerant("tomato", 1, 0.05)
carrot = classes.Accelerant("carrot", 1, 0.04)
potato = classes.Accelerant("potato", 1, 0.05)
corn = classes.Accelerant("corn", 2, 0.08)
wheat = classes.Accelerant("wheat", 1, 0.06)
strawberry = classes.Accelerant("strawberry", 0.5, 0.07)
apple = classes.Accelerant("apple", 1, 0.09)
watermelon = classes.Accelerant("watermelon", 6, 0.2)

# list so its easier to randomize
all_crops = [
    grow_accel, pumpkin, melon, tomato, carrot, potato, corn, wheat,
    strawberry, apple, watermelon
]

# seeds
pumpkin_seed = classes.Seed("pumpkin seed", 1, random.randint(1, 3), pumpkin)
melon_seed = classes.Seed("melon seed", 1, random.randint(1, 3), melon)
tomato_seed = classes.Seed("tomato seed", 0.5, 1, tomato)
carrot_seed = classes.Seed("carrot seed", 0.5, 1, carrot)
potato_seed = classes.Seed("potato seed", 0.5, random.randint(1, 2), potato)
corn_seed = classes.Seed("corn seed", 0.5, random.randint(2, 3), corn)
wheat_seed = classes.Seed("wheat seed", 0.5, random.randint(1, 2), wheat)
strawberry_seed = classes.Seed("strawberry seed", 0.5, random.randint(1, 2), strawberry)
apple_seed = classes.Seed("apple seed", 0.5, random.randint(2, 4), apple)
watermelon_seed = classes.Seed("watermelon seed", 1, random.randint(2, 4), watermelon)

# same thing as with crops
all_seeds = [
    pumpkin_seed, melon_seed, tomato_seed, carrot_seed, potato_seed,
    corn_seed, wheat_seed, strawberry_seed, apple_seed,
    watermelon_seed
]


shop_pool = all_seeds + all_crops
# randomize shop pool
def restock_shop(count=6):
    return random.sample(shop_pool, count)