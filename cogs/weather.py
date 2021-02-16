import discord
from discord.ext import commands
import string
from pyowm.owm import OWM
from datetime import datetime

owm = OWM("d346fc2bf2d9648ed0928ace4c31d1aa")

class weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="Shows the weather stats of a city given. This range is massive so feel free to mention small towns as well. Ex: `b weather dallas`")
    
    async def weather(self, ctx, *, place):
        " ".join(place)
        mgr = owm.weather_manager()
        observe = mgr.weather_at_place(place)
        weather = observe.weather
        embed = discord.Embed(
            title = f"Weather in {string.capwords(place)}",
            description = f"{weather.detailed_status.capitalize()}",
            color = 0xffe135
        )
        temperature = weather.temperature(unit='fahrenheit')
        pressure = weather.pressure
        wind = weather.wind(unit = 'miles_hour')
        embed.add_field(name = "Temperature", value = f"""
            :thermometer:Temp **{temperature['temp']}** °F
            :sweat:Feels like **{temperature['feels_like']}** °F
            :small_red_triangle:Max **{temperature['temp_max']}** °F
            :small_red_triangle_down:Min **{temperature['temp_min']}** °F
        """)
        embed.add_field(name = "Other Info", value = f"""
            :sweat_drops:Humidity **{weather.humidity}**%
            :cloud_tornado:Air Pressure **{pressure['press']}** mbar
            :wind_blowing_face:Wind Speed **{round(wind['speed'])}** mph
            :compass:Bearing **{wind['deg']}** °
            :telescope:Visibility **{weather.visibility_distance}** meters
        """)
        embed.add_field(name = "Sunrise & Sunset", value = f"""
            :sunrise: Sunrise: **{datetime.utcfromtimestamp(weather.sunrise_time(timeformat = 'unix') + weather.utc_offset).strftime('%#I:%M %p')}**
            :city_sunset: Sunset: **{datetime.utcfromtimestamp(weather.sunset_time(timeformat = 'unix') + weather.utc_offset).strftime('%#I:%M %p')}**
        """)

        await ctx.send(embed = embed)
        







def setup(client):
    client.add_cog(weather(client))